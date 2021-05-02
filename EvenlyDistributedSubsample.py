import math
import itertools
import numpy as np
from sklearn.cluster import KMeans
import time

# Returns the distance between the points a and b
# For now we assume we have a flat metric
# and we are in 1D so this distance is simply |b - a|
def distance(a, b):
    return abs(b - a)

# Returns the first index of the following group of values in the list
# Assuming lst is made of groups of identical numbers, 
# as in the case of labels from k-clustering
def nextGroup(lst, i):
    val = lst[i]
    while i < len(lst) and lst[i] == val:
        i += 1
    return i

# Given a sorted list, return the entry closest to val
# If two values are equidistant from a cluster's mean we arbitrarily choose to return the larger one
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
# This can be defined in various ways

# Option 1: Minimize the difference between 
            # the distance between the two most distant points and
            # the distance between the two closest points
def cost1(subsample):
    mindist = math.inf
    maxdist = - math.inf
    for i in range(len(subsample)-1):
        dist = distance(subsample[i], subsample[i+1])
        mindist = min(mindist, dist)
        maxdist = max(maxdist, dist)
    return maxdist - mindist

# Handle the base cases separately:
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
def optimalSubsample_bruteforce(sample, N):
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
        tmpcost = cost1(subsample)
        if tmpcost == 0: # Minimum possible cost1, no need to keep searching
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
    kmeans = KMeans(n_clusters=N).fit(sample2D) # could play with different values for n_init
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

'''
Provided examples:
optimalSubsample([0, 1, 2, 3, 4, 100], 2) => [0,100] // Always two extreme ends for 2
optimalSubsample([0, 1, 2, 3, 4, 100], 3) => [0, 4, 100]
optimalSubsample([0, 1, 2, 3, 4, 100], 4) => [0, 2, 4, 100]
'''
# We assume that the sample is sorted
# Try a few examples:
print("Brute force method, minimizing the difference", \
    "between the greatest and smallest neighbor distances:")
# Note that the brute force method will not scale well
print(optimalSubsample_bruteforce([0, 1, 2, 3, 4, 100], 2))
print(optimalSubsample_bruteforce([0, 1, 2, 3, 4, 100], 3))
print(optimalSubsample_bruteforce([0, 1, 2, 3, 4, 100], 4))
print(optimalSubsample_bruteforce([0, 1, 2, 3, 4, 100], 5))
print(optimalSubsample_bruteforce([0, 1, 2, 3, 4, 7, 15, 25], 5))
print(optimalSubsample_bruteforce([0, 1, 2, 3, 4, 7, 15, 25], 7))
print(optimalSubsample_bruteforce([0, 1, 2, 3, 4, 7, 15, 25], 9))
print(optimalSubsample_bruteforce([i*5 for i in range(10)], 8))
# Note that the k-clustering method can yield different results since it uses a different
# metric for what is considered to be "even" 
print("Using k-clustering:")
print(optimalSubsample([0, 1, 2, 3, 4, 100], 2))
print(optimalSubsample([0, 1, 2, 3, 4, 100], 3))
print(optimalSubsample([0, 1, 2, 3, 4, 100], 4))
print(optimalSubsample([0, 1, 2, 3, 4, 100], 5))
print(optimalSubsample([0, 1, 2, 3, 4, 7, 15, 25], 5))
print(optimalSubsample([0, 1, 2, 3, 4, 7, 15, 25], 7))
print(optimalSubsample([0, 1, 2, 3, 4, 7, 15, 25], 9))
print(optimalSubsample([i*5 for i in range(10)], 8))
print(optimalSubsample([i*5 for i in range(50)], 8))
print(optimalSubsample([i*5 for i in range(50)], 40))
