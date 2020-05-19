# Time: O()     ms      %
# Memory: O()   MB      %
from typing import *


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def change(w):
            out = [0] * 26
            for i in w:
                out[ord(i)-ord('a')] += 1
            return out
        standard = change(p)
        start = change(s[:len(p)])
        if start == standard:
            ans = [0]
        else:
            ans = []
        for pl in range(1, len(s)-len(p)+1):
            pr = pl + len(p) - 1
            start[ord(s[pl-1]) - ord('a')] -= 1
            start[ord(s[pr]) - ord('a')] += 1
            if start == standard:
                ans.append(pl)
        return ans
