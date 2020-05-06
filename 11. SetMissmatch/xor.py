# Time: O(n)     288ms
# Memory: O(1)   15MB
# Use xor to significantly decrease the space usage (theoretically)
# [important]

from typing import *


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = 0
        for i in range(n):  # xor all in nums and range(1, n+1
            ans ^= i + 1
            ans ^= nums[i]
        count = 0
        while ans > 0:  # count which bit is the first 1
            ans = ans >> 1
            count += 1
        ans1 = 0
        ans2 = 0
        for i in range(n):  # the bit `count` is the bit two lists differ. So split them into two sets.
            if nums[i] & pow(2, count-1):
                ans1 ^= nums[i]
            else:
                ans2 ^= nums[i]
            if (i+1) & pow(2, count-1):
                ans1 ^= i+1
            else:
                ans2 ^= (i+1)
        if ans1 in nums:
            return [ans1, ans2]
        else:
            return [ans2, ans1]


if __name__ == '__main__':
    s = Solution()
    print(s.findErrorNums([1, 2, 2, 4]))
