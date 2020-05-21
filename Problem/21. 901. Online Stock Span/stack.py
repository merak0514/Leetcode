# Time: O(1) for average time (each element can be pop for at most once)     456ms     77%
# Memory: O(n)   18.5MB      100%
from typing import *


class StockSpanner:

    def __init__(self):
        self. stack = []

    def next(self, price: int) -> int:
        weight = 1
        while self.stack[-1][0] <= price or not self.stack:
            weight += self.stack.pop()[1]
        self.stack.append((price, weight))
        return weight


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
