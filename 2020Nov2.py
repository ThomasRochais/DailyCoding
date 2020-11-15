import random

class Solution:
    def solve(self, nums):
        l = len(nums)
        prod1 = [1] * l
        prod2 = [1] * l
        products = [1] * l
        p1 = 1
        p2 = 1
        i = 0
        j = l - 1
        while i < l - 1:
            p1 *= nums[i]
            p2 *= nums[j]
            prod1[i + 1] = p1
            prod2[j - 1] = p2
            i += 1
            j -= 1
        for i in range(l):
            products[i] = prod1[i] * prod2[i]
        return products

nums_list = [[1, 2, 3, 4, 5],[3, 2, 1]]
for i in range(len(nums_list)):
    print(Solution().solve(nums_list[i]))