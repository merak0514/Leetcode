# Time: O(n^3)     Time Limit Exceeded
# Memory: O()   MB
# I thought it would be better, but in fact it becomes worse
# In fact, if you think the comparison step (is pa) is O(1), then this is an O(n^2)

from typing import *
import math


class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        m = 0
        s_c = []

        s = list(s)
        list_left = []
        list_right = []
        for i in range(len(s)):
            list_left = s[i: i + (length - i) // 2]
            list_right = s[i + math.ceil((length - i) / 2):][::-1]

            for j in range(len(s), i-1, -1):  # j is the relative index
                current_length = j - i
                if list_left == list_right:  # is pa
                    if current_length > m:
                        s_c = s[i: j]
                        m = current_length
                        # print(s_c, m)

                list_right = list_right[1:]
                if current_length % 2 == 0:  # even
                    list_left = list_left[:-1]
                else:  # odd
                    list_right.append(s[i + current_length // 2])

        return ''.join(s_c)
