# Time: O(n)     64ms
# Memory: O(n)   15MB
from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def findTarget(self, root: TreeNode, k: int) -> bool:
        pool = set()

        def find(r):
            if not r:
                return False
            v = r.val
            if (k - v) in pool:
                return True
            pool.add(v)
            return find(r.left) or find(r.right)

        return find(root)
