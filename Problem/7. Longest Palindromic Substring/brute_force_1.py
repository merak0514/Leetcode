# Time: O(n^3)     Time Limit Exceeded
# Memory: O()   MB
from typing import *


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_pa(ss: str) -> bool:
            l = len(ss)
            for i in range(int(l/2) + 1):
                if ss[i] is not ss[-i - 1]:
                    return False
            return True
        m = 0
        s_c = ''
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if is_pa(s[i: j]) and j - i > m:
                    m = j - i
                    s_c = s[i: j]
        return s_c
