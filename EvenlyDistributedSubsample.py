import math
import itertools
import numpy as np
from sklearn.cluster import KMeans

# Returns the distance between the points a and b
# For now we assume we have a flat metric
# and we are in 1D so this distance is simply |b - a|
def distance(a, b):
    return abs(b - a)

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
def optimalSubsample1(sample, N):
    if N <= 2 or N >= len(sample):
        return baseCases(sample, N)
    # For N > 2 (but less than the sample size):
    cost = math.inf
    res = []
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
# If two values are equidistant from a cluster's mean we arbitrarily choose to return the smaller one
def optimalSubsample2(sample, N):
    l = len(sample)
    if N <= 2 or N >= l:
        return baseCases(sample, N)
    # For N > 2 (but less than the sample size):
    res = []
    sample2D = np.reshape(sample, (l, 1))
    kmeans = KMeans(n_clusters = N).fit(sample2D) # could play with different values for n_init
    labels = kmeans.labels_
    i = 0
    while i < l:
        j = 0
        lab = labels[i]
        while i+j < l and labels[i+j] == lab:
            j += 1
        res.append(sample[i + ((j-1)//2)])
        i += j
    return res


'''
Examples:
optimalSubsample([0, 1, 2, 3, 4, 100], 2) => [0,100] // Always two extreme ends for 2
optimalSubsample([0, 1, 2, 3, 4, 100], 3) => [0, 4, 100]
optimalSubsample([0, 1, 2, 3, 4, 100], 4) => [0, 2, 4, 100]
'''
# Assume that the sample is sorted
# Try a few examples:
print("Brute force method, minimizing the difference", \
    "between the greatest and smallest neighbor distances:")
print(optimalSubsample1([0, 1, 2, 3, 4, 100], 2))
print(optimalSubsample1([0, 1, 2, 3, 4, 100], 3))
print(optimalSubsample1([0, 1, 2, 3, 4, 100], 4))
print(optimalSubsample1([0, 1, 2, 3, 4, 100], 5))
print(optimalSubsample1([0, 1, 2, 3, 4, 7, 15, 25], 5))
print(optimalSubsample1([0, 1, 2, 3, 4, 7, 15, 25], 7))
print(optimalSubsample1([0, 1, 2, 3, 4, 7, 15, 25], 9))
print("Using k-clustering:")
print(optimalSubsample2([0, 1, 2, 3, 4, 100], 2))
print(optimalSubsample2([0, 1, 2, 3, 4, 100], 3))
print(optimalSubsample2([0, 1, 2, 3, 4, 100], 4))
print(optimalSubsample2([0, 1, 2, 3, 4, 100], 5))
print(optimalSubsample2([0, 1, 2, 3, 4, 7, 15, 25], 5))
print(optimalSubsample2([0, 1, 2, 3, 4, 7, 15, 25], 7))
print(optimalSubsample2([0, 1, 2, 3, 4, 7, 15, 25], 9))