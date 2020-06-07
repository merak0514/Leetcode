# Time: O(n^3)     ms      %
# Memory: O()   MB      %
from typing import *
from functools import lru_cache

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        M = pow(10, 10)
        if target > m:
            return -1
        p = []
        choice = list(range(1, n + 1))

        @lru_cache(None)
        def compute(pre, posi, tar):
            if tar < 0:
                return M
            if posi == m and tar != 0:
                return M
            if posi == m:
                return 0
            if houses[posi]:
                if houses[posi] == pre:
                    return compute(houses[posi], posi + 1, tar)
                else:
                    return compute(houses[posi], posi + 1, tar - 1)

            possible = []
            for i in range(1, n + 1):
                if i == pre:
                    same = cost[posi][pre - 1] + compute(pre, posi + 1, tar)
                    possible.append(same)
                else:
                    possible.append(cost[posi][i - 1] + compute(i, posi + 1, tar - 1))
            return min(possible)

        if houses[0]:
            p.append(compute(houses[0], 1, target - 1))
        else:
            for i in choice:
                p.append(cost[0][i - 1] + compute(i, 1, target - 1))
        # print(p)
        if min(p) < M:
            return min(p)
        else:
            return -1


if __name__ == '__main__':
    s = Solution()
    par = [([3, 1, 2, 3], [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], 4, 3, 3),
           ]
    a, b, c, d, e = par[0]
    print(s.minCost(a, b, c, d, e))
