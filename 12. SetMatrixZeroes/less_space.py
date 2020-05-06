# Time: O(mn)     -ms      %
# Memory: O(1)   14.2MB      5%  Strange! Something wrong with the platform.
# Use the first row as indicator
from typing import *


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        f_l = 1
        if 0 in matrix[0]:
            f_l = 0
        for i in range(1, m):
            flag = 1
            for j in range(n):
                if not matrix[i][j]:
                    flag = 0
                    # matrix[i][0] = 0
                    matrix[0][j] = 0
            if not flag:
                matrix[i] = [0] * n
        for i in range(n):
            if not matrix[0][i]:
                for line in matrix:
                    line[i] = 0
        if not f_l:
            matrix[0] = [0] * n
