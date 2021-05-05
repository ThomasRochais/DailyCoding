import math
import itertools
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial import KDTree

# Returns the distance between the points a and b
# For now we assume we have a flat metric
# and we are in 1D so this distance is simply |b - a|
def distance(a, b):
    return abs(b - a)

# The cost function to be minimized to ensure that
# the selected values are "as evenly distributed as possible"
# This could be defined in various ways

# Option 1: Minimize the difference between 
            # the distance between the two most distant points and
            # the distance between the two closest points
# This cost function has O(len(subsample)) time complexity
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

'''
Optimized solution begins here
'''
def optimalSubsample(sample, N):
    l = len(sample)
    if N <= 2 or N >= l:
        return baseCases(sample, N)
    # For N > 2 (but less than the sample size):
    ideal_values = np.reshape([sample[0]+i*(sample[-1]-sample[0])/(N-1) for i in range(N)], (N, 1))
    sample2D = np.reshape(sample, (l, 1))
    sampleTree = KDTree(sample2D) # for quick nearest-neighbor lookup
    res = [] # The result subsample
    count = 0 # Count how many naive ideal_values cannot be found so we can look for others from sample
    for i in range(len(ideal_values)):
        sub = sample[sampleTree.query(ideal_values[i])[1]] # Nearest neighbor to select for subsample
        if sub not in res: # Making sure it hasn't been picked yet
            res.append(sub)
        else: # We're going to have to do something else
            count += 1
    if count > 0: # We have to take a few more values from sample
        remains = [] # Values that belong to sample but not the subsample res
        for s in sample:
            if s not in res:
                remains.append(s)
        # Use k-means clustering to evenly pick the remaining entries:
        remains2D = np.reshape(remains, (len(remains), 1))
        remainsTree = KDTree(remains2D)
        kmeans = KMeans(n_clusters=count).fit(remains2D) # could play with n_init
        centers = kmeans.cluster_centers_.flatten()
        for i in range(count):
            res.append(remains[remainsTree.query(centers[i])[1]])
        res.sort() # Sort back for presentation purposes
    return res

# We assume that the sample is sorted
# Try a few examples:
print("Brute force method, minimizing the difference", \
    "between the greatest and smallest neighbor distances:")
# Note that the brute force method will not scale well with sample size
# print(optimalSubsample_bruteforce([0, 1, 2, 3, 4, 100], 2))
# print(optimalSubsample_bruteforce([0, 1, 2, 3, 4, 100], 3))
# print(optimalSubsample_bruteforce([0, 1, 2, 3, 4, 100], 4))
# print(optimalSubsample_bruteforce([0, 1, 2, 3, 4, 100], 5))
# print(optimalSubsample_bruteforce([0, 25, 33, 50, 66, 75, 100], 2))
# print(optimalSubsample_bruteforce([0, 25, 33, 50, 66, 75, 100], 3))
# print(optimalSubsample_bruteforce([0, 25, 33, 50, 66, 75, 100], 4))
# print(optimalSubsample_bruteforce([0, 25, 33, 50, 66, 75, 100], 5))
print(optimalSubsample_bruteforce([0, 1, 2, 3, 4, 7, 15, 25], 5))
print(optimalSubsample_bruteforce([0, 1, 2, 3, 4, 7, 15, 25], 7))
# print(optimalSubsample_bruteforce([i*5 for i in range(10)], 8))
print("Using naive plus KMeans")
# print(optimalSubsample([0, 1, 2, 3, 4, 100], 2))
# print(optimalSubsample([0, 1, 2, 3, 4, 100], 3))
# print(optimalSubsample([0, 1, 2, 3, 4, 100], 4))
# print(optimalSubsample([0, 1, 2, 3, 4, 100], 5)) # The output can vary here, depending on what is considered "even"
# print(optimalSubsample([0, 25, 33, 50, 66, 75, 100], 2))
# print(optimalSubsample([0, 25, 33, 50, 66, 75, 100], 3))
# print(optimalSubsample([0, 25, 33, 50, 66, 75, 100], 4))
# print(optimalSubsample([0, 25, 33, 50, 66, 75, 100], 5))
print(optimalSubsample([0, 1, 2, 3, 4, 7, 15, 25], 5))
print(optimalSubsample([0, 1, 2, 3, 4, 7, 15, 25], 7))
# print(optimalSubsample([i*5 for i in range(10)], 8))