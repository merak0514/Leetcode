# Time: O(n^3)     Time Limit Exceeded
# Memory: O()   MB
# It is worse than bf2 according to test_6, while it is better by the tests from leetcode
from typing import *
import math


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_pa(ss: str) -> bool:
            l = len(ss)
            s_l = ss[:l//2]
            s_r = ss[math.ceil(l / 2):][::-1]
            if s_l == s_r:
                return True
            return False
        m = 0
        s_c = ''
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if is_pa(s[i: j]) and j - i > m:
                    m = j - i
                    s_c = s[i: j]
        return s_c
