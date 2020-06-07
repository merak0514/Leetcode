# Time: O(n)     ms      %
# Memory: O()   MB      %
from typing import *


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        son_table = [[] for _ in range(n)]
        father_table = [[] for _ in range(n)]
        for i in connections:
            son_table[i[0]].append(i[1])
            father_table[i[1]].append(i[0])

        def compute(cu, pre):
            if cu != 0 and len(father_table[cu]) + len(son_table[cu]) == 1:
                return 0
            count = 0
            for i in father_table[cu]:
                if i != pre:
                    count += compute(i, cu)
            for j in son_table[cu]:
                if j != pre:
                    count += compute(j, cu) + 1
            return count
        return compute(0, -1)


if __name__ == '__main__':
    s = Solution()
    par = [[6, [[0,1],[1,3],[2,3],[4,0],[4,5]]],
           ]
    a, b = par[0]
    print(s.minReorder(a, b))
