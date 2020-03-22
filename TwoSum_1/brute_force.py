# Time: O(n^2) 5264ms
# Memory: O(1) 13.6MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for k, i in enumerate(nums):
            for k2, j in enumerate(nums[k+1:]):
                if i + j == target:
                    return k, k2+k+1