# Time: O()     64ms      %
# Memory: O()   MB      %
# 1441
from typing import *


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        push = "Push"
        pop = "Pop"
        ans = []
        count = 0
        for i in range(1, target[-1] + 1):
            ans.append(push)
            if i == target[count]:
                count += 1
            else:
                ans.append(pop)
        return ans