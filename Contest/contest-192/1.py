# 1470. Shuffle the Array
# Time: O()     ms      %
# Memory: O()   MB      %
from typing import *


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(int(len(nums) / 2)):
            ans.append(nums[i])
            ans.append(nums[i + int(len(nums) / 2)])
        return ans
