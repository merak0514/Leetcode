# Time: O(n^2)     392ms
# Memory: O(n)   13MB
# Brute force
from typing import *


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if l == 0:
            return 0
        appeared = set()

        def fromStart(s: str):
            appeared.clear()
            for i in s:
                if i in appeared:
                    break
                appeared.add(i)

        m = [0] * l
        m[-1] = 1
        appeared.add(s[-1])
        for i in range(l - 2, -1, -1):
            if s[i] not in appeared:
                appeared.add(s[i])
                count = len(appeared)
                m[i] = count if count > m[i + 1] else m[i + 1]
            else:
                fromStart(s[i:])
                count = len(appeared)
                m[i] = count if count > m[i + 1] else m[i + 1]
        return m[0]
