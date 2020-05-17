# Time: O()     ms      %
# Memory: O()   MB      %
from typing import *
from functools import lru_cache


@lru_cache(128)
def prime(a, b):
    if a == 1 or b == 1:
        return 1
    while b:
        temp = b
        b = a % b
        a = temp
    if a == 1:
        return 1
    else:
        return 0


class Solution(object):
    def simplifiedFractions(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rt = []
        for i in range(2, n+1):
            for j in range(1, i):
                if prime(i, j):
                    rt.append('/'.join([str(j), str(i)]))
        return rt

if __name__ == '__main__':
    s = Solution()
    print(s.simplifiedFractions(2))
