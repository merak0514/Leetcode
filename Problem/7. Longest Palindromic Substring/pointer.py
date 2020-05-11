# Time: O(n^2)     804ms
# Memory: O(1)   12.8MB
from typing import *


class Solution:
    def longestPalindrome(self, s: str) -> str:
        p_l = 0  # pointer
        p_r = 0
        for p_c in range(len(s)):  # odd part
            p_l_tmp = p_c
            p_r_tmp = p_c
            remaining = min(p_c, len(s) - p_c - 1)
            for j in range(1, 1+remaining):
                if s[p_l_tmp-1] == s[p_r_tmp+1]:
                    p_l_tmp -= 1
                    p_r_tmp += 1
                    continue
                else:
                    break
            if (p_r_tmp-p_l_tmp) > (p_r-p_l):
                p_r = p_r_tmp
                p_l = p_l_tmp
        for p_c in range(len(s) - 1):  # even part
            p_l_tmp = p_c
            p_r_tmp = p_c + 1
            if s[p_l_tmp] != s[p_r_tmp]:  # less than 2
                continue
            remaining = min(p_c, len(s) - p_c - 2)
            for j in range(1, 1+remaining):
                if s[p_l_tmp-1] == s[p_r_tmp+1]:
                    p_l_tmp -= 1
                    p_r_tmp += 1
                    continue
                else:
                    break
            if (p_r_tmp - p_l_tmp) > (p_r - p_l):
                p_r = p_r_tmp
                p_l = p_l_tmp

        return s[p_l: p_r + 1]
