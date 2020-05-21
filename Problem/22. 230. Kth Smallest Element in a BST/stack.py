# Time: O(H+k)     ms      %
# Memory: O(H+k)   MB      %
# Important: How to iterate over BST from the left to the right
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
            if not root and not stack:
                return -1


if __name__ == '__main__':
    t = TreeNode(3)
    t.left = TreeNode(1)
    t.left.right = TreeNode(2)
    t.right = TreeNode(4)
    s = Solution()
    print(s.kthSmallest(t, 2))
