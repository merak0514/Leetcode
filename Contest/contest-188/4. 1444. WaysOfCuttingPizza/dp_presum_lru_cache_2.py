# Time: O()     236ms      90%
# Memory: O()   15.6MB      100%
# use lru_cache to automatically construct memory. Use the default parameter (128)
from typing import *
from functools import lru_cache


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n, mo = len(pizza), len(pizza[0]), 1000000007
        pre_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                pre_sum[i][j] = (pizza[i][j] == 'A') + pre_sum[i][j + 1] + \
                                pre_sum[i + 1][j] - pre_sum[i + 1][j + 1]

        @lru_cache(None)  # very important, automatically save the result. When querying,
        # firstly search in the cache if there is the same parameter computed
        def dp(y, x, cut):
            if not pre_sum[y][x]:
                return 0
            if not cut:
                return 1
            ans = 0
            for yy in range(y + 1, m):
                if pre_sum[y][x] - pre_sum[yy][x] > 0:
                    ans = (ans + dp(yy, x, cut - 1)) % mo
            for xx in range(x + 1, n):
                if pre_sum[y][x] - pre_sum[y][xx] > 0:
                    ans = (ans + dp(y, xx, cut - 1)) % mo
            return ans % mo

        return dp(0, 0, k - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.ways([".A","AA","A."], 3))
