# 1464. Maximum Product of Two Elements in an Array
# Time: O()     ms      %
# Memory: O()   MB      %
from typing import *

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1 = 0
        m2 = 0
        for i in nums:
            if i > m1:
                m2 = m1
                m1 = i
            elif i > m2:
                m2 = i
        return (m1-1) * (m2-1)
