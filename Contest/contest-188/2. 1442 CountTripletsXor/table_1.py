# Time: O(n^3)     2440ms      53.6%
# Memory: O(n^2)   15.2MB      %
from typing import *


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        table = [[0]*n for _ in range(n)]
        for p in range(n):
            table[p][p] = arr[p]
            for q in range(p+1, n):
                table[p][q] = table[p][q-1] ^ arr[q]
        count = 0
        # ans = []
        for i in range(n):
            for j in range(i+1, n):
                target = table[i][j-1]
                for k in range(j, n):
                    if table[j][k] == target:
                        count += 1
        #                 ans.append((i, j, k))
        # print(count)
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.countTriplets([7,11,12,9,5,2,7,17,22]))
