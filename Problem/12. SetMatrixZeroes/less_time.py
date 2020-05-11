# Time: O(m*n)     128ms        96%
# Memory: O()      14.3MB              5%
# Note: this question is mainly focusing on reducing space complexity
from typing import *


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zeros = [0] * n
        l2 = []
        for i in range(m):
            flag = 1
            for j in range(n):
                if not matrix[i][j]:
                    flag = 0
                    l2.append(j)
            if not flag:
                matrix[i] = zeros
        for k in l2:
            for line in matrix:
                line[k] = 0

