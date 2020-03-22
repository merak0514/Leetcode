# Time: O(n) 48ms
# Memory: O(n) 14.3MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for k, i in enumerate(nums):
            find = target - i
            if find in hashmap.keys():
                return [k, hashmap[find]]
            else:
                hashmap[i] = k