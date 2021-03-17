import numpy as np
from math import prod

def maxArea(mat):
    if np.all(mat):
        return prod(mat.shape)
    elif ~np.any(mat.flatten()):
        return 0
    else:
        return max(maxArea(mat[:,0:-1]), maxArea(mat[:,1:]), maxArea(mat[0:-1,:]), maxArea(mat[1:,:]))

M = np.random.randint(0,2,(4,3))
N = np.array([[1,0,0,0],[1,0,1,1],[1,0,1,1],[0,1,0,0]])
K = np.ones((4,4))
print(M)
print(maxArea(M))
print(maxArea(N))
print(maxArea(K))