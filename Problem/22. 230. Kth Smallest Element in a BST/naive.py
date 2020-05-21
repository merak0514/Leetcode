# Time: O()     ms      %
# Memory: O()   MB      %
# extend the tree to a ordered list
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def iterate(r):
            if r:
                return iterate(r.left) + [r.val] + iterate(r.right)
            else:
                return []
        return iterate(root)[k-1]

if __name__ == '__main__':
    t = TreeNode(3)
    t.left = TreeNode(1)
    t.left.right = TreeNode(2)
    t.right = TreeNode(4)
    s = Solution()
    print(s.kthSmallest(t, 2))
