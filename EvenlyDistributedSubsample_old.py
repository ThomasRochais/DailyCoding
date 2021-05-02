import math
import random
from sklearn.neighbors import NearestNeighbors
import numpy as np

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
        dist = distance(subsample[i], subsample[i-1])
        mindist = min(mindist, dist)
        maxdist = max(maxdist, dist)
    return maxdist - mindist

# Option 2: Minimize the nearest-neighbor distance functions
def cost2(sample, subsample):
    maxdist = -math.inf
    dictsample = {k: v for v, k in enumerate(sample)}
    for v in subsample:
        index = dictsample[v]
        if index == 1:
            maxdist = max( maxdist, distance(v, sample[index+1]) )
        if index == len(sample)-1:
            maxdist = max( maxdist, distance(v, sample[index-1]) )
        else:
            maxdist = max(maxdist, 
                          min(distance(v, sample[index-1]), distance(v, sample[index+1]) )
            )
    return maxdist
    


# From the examples, it appears we also want to maximize the spread of the subsample
# Thus we always include the first and last values from the sample
def optimalSubsample(sample, N):
    if N <= 0:
        return []
    if N == 1:
        return sample[len(sample) // 2]
    if N == 2:
        return [sample[0], sample[-1]]
    # For N > 2:
    subsample = [sample[0]]
    subsample.extend(random.sample(sample[1:-1], N-2))
    subsample.append(sample[-1])
    print(subsample, cost1(subsample))
    print(subsample, cost2(sample, subsample))
    return(subsample)

'''
Examples:
optimalSubsample([0, 1, 2, 3, 4, 100], 2) => [0,100] // Always two extreme ends for 2
optimalSubsample([0, 1, 2, 3, 4, 100], 3) => [0, 4, 100]
optimalSubsample([0, 1, 2, 3, 4, 100], 4) => [0, 2, 4, 100]
'''

optimalSubsample([0, 1, 2, 3, 4, 100], 3)