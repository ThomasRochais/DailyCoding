import random
import math

class Solution:
    def solve(self, N, error):
        r = 1 # Radius of the circle
        pival = 1
        delta = abs(math.pi - pival)
        i = 0 # All random darts counter
        c = 0 # Circle counter
        while delta > error and i <= N:
            x = random.uniform(0,1) 
            y = random.uniform(0,1)
            i += 1
            if x*x + y*y <= 1:
                c += 1
            # Area of circle / Area of (surrounding) square = pi / 4
            pival = c / i * 4
            delta = abs(math.pi - pival)
        return pival, delta, i
sol = Solution()
N = 10000 # Max number of operations (darts thrown)
error = 0.001 # Allowed error
print(sol.solve(N, error))