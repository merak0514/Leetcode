# Time: O(mn) for init and O(1) for per query     108ms      90.3%
# Memory: O(mn)   17.2MB      16.67%
from typing import *


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        m = len(matrix)
        n = len(matrix[0])
        self.matrix = matrix
        self.summation = [[0] * (n+1) for _ in range(m+1)]  # Add two padding on the left and upper boundaries
        for i in range(m):
            for j in range(n):
                self.summation[i+1][j+1] = matrix[i][j] + self.summation[i][j+1] +\
                                           self.summation[i+1][j] - self.summation[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.summation[row2+1][col2+1] - self.summation[row1][col2+1] - \
               self.summation[row2+1][col1] + self.summation[row1][col1]


if __name__ == '__main__':
    matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
    obj = NumMatrix(matrix)
    test = [[2,1,4,3],[1,1,2,2],[1,2,2,4]]
    a, b, c, d = test[0]
    print(obj.sumRegion(a, b, c, d))


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
