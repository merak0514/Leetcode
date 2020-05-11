# Time: O(n) 60ms
# Memory: O(n) 13.3MB
# The same as the one in TwoSum_1/brute_force.py
from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for k, i in enumerate(nums):
            find = target - i
            if find in hashmap.keys():
                return [k, hashmap[find]]
            else:
                hashmap[i] = k