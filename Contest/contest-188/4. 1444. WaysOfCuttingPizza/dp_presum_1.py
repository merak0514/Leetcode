# Time: O()     340ms      71.22%
# Memory: O()   14.2MB      100%
# build memory by hand to memorize repeated outcomes
from typing import *


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n, mo = len(pizza), len(pizza[0]), 1000000007
        pre_sum = [[0] * (n + 1) for _ in range(m + 1)]
        memory = [[[-1] * k for _ in range(n)] for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                pre_sum[i][j] = (pizza[i][j] == 'A') + pre_sum[i][j + 1] + \
                                pre_sum[i + 1][j] - pre_sum[i + 1][j + 1]

        def dp(y, x, cut):
            if not pre_sum[y][x]:
                return 0
            if not cut:
                return 1
            if memory[y][x][cut] != -1:
                return memory[y][x][cut]
            ans = 0
            for yy in range(y + 1, m):
                if pre_sum[y][x] - pre_sum[yy][x] > 0:
                    ans = (ans + dp(yy, x, cut - 1)) % mo
            for xx in range(x + 1, n):
                if pre_sum[y][x] - pre_sum[y][xx] > 0:
                    ans = (ans + dp(y, xx, cut - 1)) % mo
            memory[y][x][cut] = ans
            return ans

        return dp(0, 0, k - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.ways([".A","AA","A."], 3))
