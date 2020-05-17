# Time: O(2^n)  456ms     %
# Memory: O()   41MB      %
from typing import *
from functools import lru_cache


class Solution:
    def largestNumber(self, cost: List[int], target: int):

        @lru_cache(None)  # Set the parameter to `None` so that the `lru` is disabled and cache can grow `unbounded`
        def f(left):
            ma = -5000
            string = '0'
            for i in range(9):
                n = left - cost[i]
                if n < 0:
                    continue
                v, tmp_string = p(left - cost[i])
                tmp = 1 + v
                if tmp >= ma:
                    ma = tmp
                    string = str(i + 1) + tmp_string
            return ma, string

        # You can put lru_cache here instead of before `f`,
        # to decrease the time to 224ms but increase the memory usage to 41.1MB
        def p(left):
            if left < 0:
                return -5000, '0'
            if left == 0:
                return 0, '0'
            else:
                return f(left)

        flag, ans = p(target)
        if flag <= 0:
            return '0'
        else:
            return ans[:-1]


if __name__ == '__main__':
    s = Solution()
    tests = [([6, 10, 15, 40, 40, 40, 40, 40, 40], 47),
             ([2, 4, 6, 2, 4, 6, 4, 4, 4], 5),
             ([7, 6, 5, 5, 5, 6, 8, 7, 8], 12),
             ([4, 3, 2, 5, 6, 7, 2, 5, 5], 9)]
    a, b = tests[3]
    print(s.largestNumber(a, b))
