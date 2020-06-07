# Time: O()     ms      %
# Memory: O()   MB      %
from typing import *


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        m = 0
        h_start = 0
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)
        for i in horizontalCuts:
            v_start = 0
            for j in verticalCuts:
                tmp = (i - h_start) * (j - v_start)
                if tmp > m:
                    m = tmp
                v_start = j
            tmp = (i - h_start) * (w - v_start)
            if tmp > m:
                m = tmp

            h_start = i

        h_start = horizontalCuts[-1]
        v_start = 0
        for j in verticalCuts:
            tmp = (h - h_start) * (j - v_start)
            if tmp > m:
                m = tmp
            v_start = j
        tmp = (h - h_start) * (w - v_start)
        if tmp > m:
            m = tmp

        return m
