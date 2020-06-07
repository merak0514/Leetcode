# Time: O()     ms      %
# Memory: O()   MB      %
from typing import *


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        M = pow(10, 9) + 7
        def compute_max(x1, x2, y1, y2, hCuts, vCuts):
            while hCuts and (hCuts[0] < x1 or hCuts[0] > y1):
                hCuts = hCuts[1:]
            if hCuts:
                return max(compute_max(x1, x2, hCuts[0], y2, hCuts[1:], vCuts),
                           compute_max(hCuts[0], x2, y1, y2, hCuts[1:], vCuts))
            while vCuts and (vCuts[0] < x2 or vCuts[0] > y2):
                vCuts = vCuts[1:]
            if vCuts:
                return max(compute_max(x1, vCuts[0], y1, y2, hCuts, vCuts[1:]),
                           compute_max(x1, x2, y1, vCuts[0], hCuts, vCuts[1:]))
            return (y1-x1) * (y2-x2)

        return compute_max(0, 0, h, w, horizontalCuts, verticalCuts) % M


if __name__ == '__main__':
    s = Solution()
    pars = [[5, 4, [1, 2, 4], [1, 3]],
            ]
    a, b, c, d = pars[0]
    print(s.maxArea(a, b, c, d))
