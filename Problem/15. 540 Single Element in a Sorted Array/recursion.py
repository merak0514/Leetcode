# Time: O()     76ms      46%
# Memory: O()   16.1MB      %
from typing import *


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def compute(nums: List[int], n):
            if n == 1:
                return nums[0]
            ind = int((n-1) / 2)
            odd = ind % 2
            if odd:
                if nums[ind-1] == nums[ind]:
                    return compute(nums[ind+1: ], ind)
                elif nums[ind+1] == nums[ind]:
                    return compute(nums[:ind], ind)
                else:
                    return nums[ind]
            else:
                if nums[ind-1] == nums[ind]:
                    return compute(nums[:ind-1], ind-1)
                elif nums[ind+1] == nums[ind]:
                    return compute(nums[ind+2:], ind-1)
                else:
                    return nums[ind]
        return compute(nums, len(nums))
