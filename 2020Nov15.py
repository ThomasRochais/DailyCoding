import random
import numpy as np
import matplotlib.pyplot as plt

class Solution:
    def solve(self, N):
        l = len(N)
        i = 0
        pick = N[i]
        while i < l - 1:
            i += 1
            p = 1 / (i + 1)
            #  pick = random.choices([pick, N[i]], weights = (1-p, p), k = 1)[0]
            if random.randrange(i) == i - 1:
                pick = N[i]
        return pick
sol = Solution()
N = range(10000)  # Number of stuff to process
array = []
trials = 1000  # Number of trials to check distribution
binNum = trials // 100
for i in range(trials):
    array.append(sol.solve(N))
np.histogram(array)
plt.hist(array, bins = binNum)
plt.title("Distribution from data stream")
plt.show()