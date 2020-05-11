# Time: O(n^2)     1104ms      30.4%
# Memory: O()   49.3MB      %
from typing import *


class Solution:

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        son_table = [[] for _ in range(n)]  # implemented as a two-direction table,
        # for you don't know whether the smaller or the greater one is the father.
        for edge in edges:
            son_table[edge[0]].append(edge[1])
            son_table[edge[1]].append(edge[0])
        print(son_table)

        def compute(node: int, father):
            happle = hasApple[node]
            ans = 0
            for i in son_table[node]:
                if i == father:
                    if len(son_table[node]) == 1:  # This node is a leaf node.
                        return 0, hasApple[node]
                else:
                    an, h_a = compute(i, node)
                    happle |= h_a
                    ans += (2 + an) * h_a
            if ans > 0 or happle:
                happle = True
            return ans, happle

        result, _ = compute(0, -1)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.minTime(7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], [0, 0, 1, 0, 1, 1, 0]))
