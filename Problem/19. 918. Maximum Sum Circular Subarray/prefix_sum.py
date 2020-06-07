# Time: O()     ms      %
# Memory: O()   MB      %
from typing import *


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        longer = A + A
        p = [0] * (2 * n)
        p[-1] = A[-1]
        count = [0] * (2 * n)
        count[-1] = 1
        for i in range(2 * n - 2, -1, -1):
            if count[i+1] < n:
                if p[i + 1] < 0:
                    p[i] = A[i % n]
                    count[i] = 1
                else:
                    p[i] = A[i % n] + p[i + 1]
                    count[i] = count[i + 1] + 1
            elif count[i + 1] == n:
                if count[i + 1] - A[(i + n) % n] < 0:
                    p[i] = A[i % n]
                    count[i] = 1
                else:
                    p[i] = p[i + 1] - A[(i + n) % n] + A[i % n]
                    count[i] = n
            else:
                raise
        print(p)
        return max(p)


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubarraySumCircular([5,-3,5]))
