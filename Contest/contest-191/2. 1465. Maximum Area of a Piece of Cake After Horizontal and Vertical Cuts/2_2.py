# Time: O(hw)     ms      %
# Memory: O()   MB      %
from typing import *


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        M = pow(10, 9) + 7
        def compute_max(h_, w_, hCuts, vCuts):
            if h_ <= 0 or w_ <= 0:
                return 0
            while hCuts and (hCuts[0] < 0 or hCuts[0] > h_):
                hCuts = hCuts[1:]
            while vCuts and (vCuts[0] < 0 or vCuts[0] > w_):
                vCuts = vCuts[1:]

            if hCuts:
                if vCuts:
                    return max(compute_max(hCuts[0], vCuts[0], hCuts[1:], vCuts[1:]),
                               compute_max(h_ - hCuts[0], vCuts[0], [h_ - i for i in hCuts[1:]], vCuts[1:]),
                               compute_max(hCuts[0], w_ - vCuts[0], hCuts[1:], [w_ - i for i in vCuts[1:]]),
                               compute_max(h_ - hCuts[0], w_ - vCuts[0], [h_ - i for i in hCuts[1:]],
                                           [w_ - i for i in vCuts[1:]]))
                return max(compute_max(hCuts[0], w_, hCuts[1:], vCuts[1:]),
                           compute_max(h_ - hCuts[0], w_, [h_ - i for i in hCuts[1:]], vCuts[1:]))
            if vCuts:
                return max(compute_max(h_, vCuts[0], hCuts[1:], vCuts[1:]),
                           compute_max(h_, w_ - vCuts[0], hCuts[1:], [w_ - i for i in vCuts[1:]]))
            else:
                return h_*w_
        return compute_max(h, w, horizontalCuts, verticalCuts)


if __name__ == '__main__':
    s = Solution()
    pars = [[5, 4, [1, 2, 4], [1, 3]],
            ]
    a, b, c, d = pars[0]
    print(s.maxArea(a, b, c, d))
