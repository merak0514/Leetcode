# Time: O()     ms      %
# Memory: O()   MB      %
from typing import *


class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0
        ma = 0
        current = 0
        count = 1
        n = len(s)
        for i in range(n):
            if s[i] == current:
                count += 1
            else:
                ma = max(ma, count)
                current = s[i]
                count = 1
        return max(ma, count)
