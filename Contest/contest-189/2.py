# Time: O()     ms      %
# Memory: O()   MB      %
from typing import *


class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.lower()
        sp = text.split(' ')
        # for i in range(1, len(sp)):
        #     x = sp[i]
        #     j = i - 1
        #     while j >= 0 and len(sp[j]) > len(x):
        #         sp[j+1] = sp[j]
        #         j = j - 1
        #     sp[j+1] = x
        sp = sorted(sp, key=len)
        ans = ' '.join(sp)
        up = ans[0].upper()
        ans = up + ans[1:]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.arrangeWords("Leetcode is cool"))
