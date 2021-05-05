import math
import itertools
import numpy as np
from sklearn.cluster import KMeans

# Returns the distance between the points a and b
# For now we assume we have a flat metric
# and we are in 1D so this distance is simply |b - a|
def distance(a, b):
    return abs(b - a)

# Returns the first index of the following group of values in the list
# Assuming lst is made of groups of identical numbers, 
# as in the case of labels from k-clustering
# This is useful for identifying the indices for the various clusters
def nextGroup(lst, i):
    val = lst[i]
    while i < len(lst) and lst[i] == val:
        i += 1
    return i

# Given a sorted list, return the entry closest to val
# If two values are equidistant from a cluster's mean
# we arbitrarily choose to return the larger one (as if rounding up)
def closest_to_mean(lst, val):
    i = 0
    while lst[i] < val:
        i += 1
    if distance(lst[i], val) <= distance(lst[i-1], val):
        return lst[i]
    else:
        return lst[i-1]

# The cost function to be minimized to ensure that
# the selected values are "as evenly distributed as possible"
# This could be defined in various ways

# Option 1: Minimize the difference between 
            # the distance between the two most distant points and
            # the distance between the two closest points
# This cost function has O(len(subsammple)) time complexity
def cost1(subsample):
    mindist = math.inf
    maxdist = - math.inf
    for i in range(len(subsample)-1):
        dist = distance(subsample[i], subsample[i+1])
        mindist = min(mindist, dist)
        maxdist = max(maxdist, dist)
    return maxdist - mindist

# Option 2: Minimize the empty-space nearest neighbor function
# i.e. the distance from an arbitrary location to the in sample to the nearest point in subsample
# Note that for the current implementations subsample always contains the first and last entries of sample
# This cost function has O(len(sample)) time complexity
def cost2(sample, subsample):
    tot_dist = 0
    sub_i = 1
    i = 1
    while i < len(sample) - 1:
        while sample[i] != subsample[sub_i]:
            tot_dist += min(distance(sample[i], subsample[sub_i]), distance(sample[i], subsample[sub_i-1]))
            i += 1
        sub_i += 1
    return tot_dist

# Handle the base cases separately
# as this is to be done the same way regardless of the method used:
def baseCases(sample, N):
    l = len(sample)
    if N <= 0:
        return []
    if N == 1:
        return sample[l // 2]
    if N == 2:
        return [sample[0], sample[-1]]
    if N >= l:
        return sample

# From the examples, it appears we also want to maximize the spread of the subsample
# Thus we always include the first and last values from the sample (which is sorted)
# Then we want to take a subsample which minimizes the cost function
# The cost_flag is used to determine which cost function to minimize
def optimalSubsample_bruteforce(sample, N, cost_flag = 1):
    if N <= 2 or N >= len(sample):
        return baseCases(sample, N)
    # For N > 2 (but less than the sample size):
    cost = math.inf
    res = []
    # This for loop goes as O(len(sample)^2)
    # Computationally it is the most expansive part, and is objectively rather inefficient
    for subset in itertools.combinations(sample[1:-1], N-2):
        subsample = [sample[0]]
        subsample.extend(subset)
        subsample.append(sample[-1])
        if cost_flag == 1:
            tmpcost = cost1(subsample)
        if cost_flag == 2:
            tmpcost = cost2(sample, subsample)
        if tmpcost == 0: # Minimum possible cost, no need to keep searching
            return subsample
        if tmpcost < cost:
            cost = tmpcost
            res = subsample
    return(res)

# We could also implement k-means clustering to "evenly" cluster the sample
# The subsample would then be made of the entries closest to the means of each cluster
# If two values are equidistant from a cluster's mean we arbitrarily choose to return the larger one
# Furthermore, to maximize the spread of the subsample, we will instead take the first and last
# values from the first and last cluster respectively (rather than choose the values closest to the mean)
def optimalSubsample(sample, N):
    l = len(sample)
    if N <= 2 or N >= l:
        return baseCases(sample, N)
    # For N > 2 (but less than the sample size):
    sample2D = np.reshape(sample, (l, 1))
    ideal_values = np.reshape([sample[0]+i*(sample[-1]-sample[0])/(N-1) for i in range(N)], (N, 1))
    kmeans = KMeans(n_clusters=N, n_init=1, init=ideal_values).fit(sample2D)
    labels = kmeans.labels_
    centers = kmeans.cluster_centers_.flatten()
    res = [sample[0]]
    start = nextGroup(labels, 0)
    end = nextGroup(labels, start)
    for i in range(1, len(centers)-1):
        res.append(closest_to_mean(sample[start:end], centers[labels[start]]))
        start = end
        end = nextGroup(labels, start)
    res.append(sample[-1])
    return res

# We assume that the sample is sorted
# Try a few examples:
print("Brute force method, minimizing the difference", \
    "between the greatest and smallest neighbor distances:")
# Note that the brute force method will not scale well with sample size
print(optimalSubsample_bruteforce([0, 25, 33, 50, 66, 75, 100], 4))
print(optimalSubsample_bruteforce([0, 25, 33, 50, 66, 75, 100], 5))
print("Brute force method, minimizing the", \
    "empty-space nearest neighbor function:")
# Note that as it uses a different metric for the definition of "even",
# the results are expected to be different
# The 3rd argument is a flag to use the second cost function instead of the default
#print(optimalSubsample_bruteforce([0, 25, 33, 50, 66, 75, 100], 4, 2))
#print(optimalSubsample_bruteforce([0, 25, 33, 50, 66, 75, 100], 5, 2))
# Note that the k-clustering method can yield different results since it uses a different
# metric for what is considered to be "even" 
print("Using k-clustering:")
print(optimalSubsample([0, 1, 2, 3, 4, 100], 4))
print(optimalSubsample([0, 25, 33, 50, 66, 75, 100], 4))
print(optimalSubsample([0, 25, 33, 50, 66, 75, 100], 5))