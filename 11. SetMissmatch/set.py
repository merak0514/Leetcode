# Time: O(n)     200ms
# Memory: O(n)   15.4MB
from typing import *


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = set()
        for i in nums:
            if i in s:
                lost = i
            else:
                s.add(i)
        return [lost, int(n * (n + 1) / 2 - sum(s))]
