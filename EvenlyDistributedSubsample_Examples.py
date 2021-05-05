import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial import KDTree

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

def optimalSubsample(sample, N):
    EPSILON = 10**(-5) # Can be useful to "round up" nearest neighbors search
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
        # sub = sample[sampleTree.query(ideal_values[i]+EPSILON)[1]] # Use EPSILON to "round up"
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
            # res.append(remains[remainsTree.query(centers[i]+EPSILON)[1]]) # Use EPSILON to "round up"
        res.sort() # Sort back for presentation purposes
    return res

# We assume that the sample is sorted
# Try a few examples:
print("Using naive plus KMeans")
print("Sample = [0, 1, 2, 3, 4, 100]")
print(optimalSubsample([0, 1, 2, 3, 4, 100], 2))
print(optimalSubsample([0, 1, 2, 3, 4, 100], 3))
print(optimalSubsample([0, 1, 2, 3, 4, 100], 4))
print(optimalSubsample([0, 1, 2, 3, 4, 100], 5)) # The output can vary here, depending on what is considered "even"
print("Sample = [0, 25, 33, 50, 66, 75, 100]")
print(optimalSubsample([0, 25, 33, 50, 66, 75, 100], 2))
print(optimalSubsample([0, 25, 33, 50, 66, 75, 100], 3))
print(optimalSubsample([0, 25, 33, 50, 66, 75, 100], 4))
print(optimalSubsample([0, 25, 33, 50, 66, 75, 100], 5))
print("Sample = [0, 1, 2, 3, 4, 7, 15, 25]")
print(optimalSubsample([0, 1, 2, 3, 4, 7, 15, 25], 5))
print(optimalSubsample([0, 1, 2, 3, 4, 7, 15, 25], 7))
print("Sample = [0, 5, 10, 15, ..., 45]")
print(optimalSubsample(list(range(0,50,5)), 8))