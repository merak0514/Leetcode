# Time: O(n)     56ms
# Memory: O(1)   13.1MB
from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pl = 0
        pr = len(nums) - 1
        while 1:
            if (nums[pl] + nums[pr]) == target:
                return [pl + 1, pr + 1]
            elif (nums[pl] + nums[pr]) > target:
                pr -= 1
            else:
                pl += 1