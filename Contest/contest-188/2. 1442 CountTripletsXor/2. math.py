# Time: O(n^2)     60ms     86 %
# Memory: O(n)   13.9MB      %
# Note that if a=b^c^d, then a^b=c^d and a^b^c=d; Use this to solve the problem in O(n^2)
from typing import *


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        summation = [0 for _ in range(n + 1)]
        for i in range(1, n+1):
            summation[i] = summation[i-1] ^ arr[i-1]
        ans = 0
        for i in range(n):
            for j in range(i+1, n+1):
                if summation[i] == summation[j]:
                    ans += j - i - 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.countTriplets([7,11,12,9,5,2,7,17,22]))