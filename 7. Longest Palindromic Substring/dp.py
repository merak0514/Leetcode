# Time: O(n^2)     6520ms
# Memory: O(n^2)   21.5MB
from typing import *


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        length = len(s)
        is_p = [[False for _ in s] for _ in s]
        for j in range(length):
            is_p[j][j] = True
            if 1 + j < length:
                is_p[j][j + 1] = s[j] == s[j + 1]
        for i in range(2, length):
            for j in range(length):
                if i + j < length:
                    is_p[j][j+i] = is_p[j+1][j+i-1] and (s[j] == s[j+i])
        for count in range(length, 1, -1):
            # print('\n',distance)
            for start in range(length - count + 1):
                if is_p[start][start + count - 1]:
                    return s[start: start + count]
        return s[0]

