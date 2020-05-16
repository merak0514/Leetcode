# Time: O(n^2)     28ms      97.2%
# Memory: O(1)   13.7MB      %
from typing import *


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'
        rest = len(num) - k
        one2ten = [str(i) for i in range(10)]
        count = 0  # deleted
        start = 0  # accepted
        while True:
            flag = 0
            for i in one2ten:
                for ind in range(start, min(start + k+1-count, len(num))):  # see below to figure out why the boundary
                    if num[ind] == i:
                        num = num[:start] + num[ind:]  # delete the char between start & ind
                        count += ind-start
                        start += 1  # accepted char
                        flag = 1
                        break
                if flag:
                    break
            if count == k:  # you have deleted k chars
                return str(int(num))
            if start == rest:  # you have accepted n-k chars
                return str(int(num[:start]))

        # return nu

if __name__ == '__main__':
    s = Solution()
    tests = [["1432219", 3], ['112', 1], ['10', 2]]
    a, b = tests[1]
    print(s.removeKdigits(a, b))
