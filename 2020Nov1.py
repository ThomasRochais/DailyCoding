import time
import random

class Solution:
    def solve(self, nums, k):
        nums.sort()
        l = len(nums)
        isSum = False
        i = 0
        j = l - 1
        while i < j:
            if nums[i] + nums[j] == k:
                #print(nums[i], nums[j], k, nums)
                return True
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1
        #print(nums[i], nums[j], k, nums)
        return isSum

N = 20
nums_list = []
k = []
elapsed = []
for i in range(N):
    k.append(random.randint(0,2000))
    nums_list.append(random.sample(range(0, 200), 10 + i * 10))
sol = Solution()
for i in range(N):
    tic = time.time()
    print(sol.solve(nums_list[i],k[i]))
    toc = time.time()
    elapsed.append(toc-tic)
    print(toc - tic)