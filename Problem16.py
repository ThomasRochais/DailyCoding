import random
class Solution:
    def __init__(self):
        self.orders = []

    def record(self, order_id):
        self.orders.append(order_id)

    def get_last(self, i):
        return self.orders[len(self.orders) - i]
sol = Solution()
print(sol.orders)
sol.record("newitem")
print(sol.orders)
sol.record("i1")
sol.record("i2")
sol.record("i3")
sol.record("i4")
sol.record("i5")
print(sol.orders)
print(sol.get_last(2))