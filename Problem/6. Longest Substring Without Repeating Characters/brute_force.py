# Time: O(n^2)     696ms
# Memory: O(n)   12.9MB
# Brute force
from typing import *


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if l == 0:
            return 0

        def fromStart(s: str) -> int:
            appeared = set()
            count = 0
            for i in s:
                if i in appeared:
                    return count
                appeared.add(i)
                count += 1
            return count

        m = [0] * l
        m[-1] = 1
        for i in range(l - 2, -1, -1):
            fs = fromStart(s[i:])
            m[i] = fs if fs > m[i + 1] else m[i + 1]

        return m[0]
