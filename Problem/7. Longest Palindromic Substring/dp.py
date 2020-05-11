# Time: O(n^2)     4256ms
# Memory: O(n^2)   20.5MB
from typing import *


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        length = len(s)
        is_p = [[False] * length for _ in s]
        # important: Can't use `[[False] * length] * length`, it becomes the copy of the list; Thus changing any
        # element in the 1st row results in changing the same elements in all other rows.
        start = 0
        end = 0
        for j in range(length):
            is_p[j][j] = True
            if 1 + j < length:
                is_p[j][j + 1] = s[j] == s[j + 1]
                if is_p[j][j + 1]:
                    start = j
                    end = j + 1
        for distance in range(2, length):
            for j in range(length - distance):
                is_p[j][j+distance] = is_p[j+1][j+distance-1] and (s[j] == s[j+distance])
                if is_p[j][j+distance]:
                    start = j
                    end = j + distance
        return s[start: end+1]
        # below is the first version, did not use the start and end pointer
        # Thus the running
        # --------------------------

        # for count in range(length, 1, -1):
        #     for start in range(length - count + 1):
        #         if is_p[start][start + count - 1]:
        #             return s[start: start + count]
        # return s[0]

