# Time: O()     ms      %
# Memory: O()   MB      %
from typing import *
from math import factorial
from functools import reduce


class Solution:
    def getProbability(self, balls: List[int]) -> float:
        def compute(pl, pr, l, r, b):
            if l < 0 or r < 0:
                return 0
            count = 0
            if pl:
                for i in b:
                    if i <= l:
                        b_c = b.copy()
                        b_c.remove(i)
                        count += compute(pl - 1, pr, l - i, r, b_c)
                return count
            if pr:
                for i in b:
                    if i <= r:
                        b_c = b.copy()
                        b_c.remove(i)
                        count += compute(pl, pr - 1, l, r - i, b_c)
                return count
            for i in b:
                if i < 2:
                    return 0
            l -= len(b)
            r -= len(b)
            if l < 0 or r < 0:
                return 0
            total = sum(b) - 2 * len(b)
            count = factorial(total) / (factorial(l) * factorial(r))
            print(count)
            return count

        k = len(balls)
        n = int(sum(balls) / 2)
        m = int(k / 2) if k % 2 == 0 else int((k + 1) / 2)
        ans = 0
        for i in range(m, k + 1):  # i colors each
            ans += compute(k - i, k - i, n, n, balls) *
        print(ans)
        denominator = factorial(2*n) / reduce(lambda x, y: factorial(x)*factorial(y), balls)
        print(denominator)
        return ans * factorial(n) * factorial(n) / denominator


if __name__ == '__main__':
    s = Solution()
    par = [[1,1],
           [2, 1, 1],
           [1, 2, 1, 2]
           ]
    a = par[2]
    print(s.getProbability(a))
