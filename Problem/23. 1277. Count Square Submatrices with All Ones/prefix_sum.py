# Time: O()     ms      %
# Memory: O()   MB      %
from typing import *


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        summation = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                summation[i + 1][j + 1] = matrix[i][j] + summation[i][j + 1] + summation[i + 1][j] - summation[i][j]
        count = 0
        for i in range(1, min(m, n) + 1):
            tmp = pow(i, 2)
            for j in range(m - i + 1):
                for k in range(n - i + 1):
                    if (summation[j + i][k + i] - summation[j][k + i] - summation[j + i][k] + summation[j][k]) == tmp:
                        count += 1
        return count
