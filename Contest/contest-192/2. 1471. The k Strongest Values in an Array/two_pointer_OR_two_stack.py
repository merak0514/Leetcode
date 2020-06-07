# Time: O(nlgn)     ms      %
# Memory: O()   MB      %
from typing import *


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        s1 = sorted(arr)  # The last one is the largest one
        s2 = s1[::-1]
        m = s1[int((n-1) / 2)]
        ans = []
        while k:
            if abs(s2[-1] - m) > abs(s1[-1] - m):
                ans.append(s2[-1])
                s2.pop()
            else:
                ans.append(s1[-1])
                s1.pop()

            k -= 1

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.getStrongest( [2, 1, 3, 4,6], 5))
