# Time: O()     ms      %
# Memory: O()   MB      %
from typing import *

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        global count
        count = 0

        def compute(ro: TreeNode, val):
            if not ro:
                return
            global count
            if ro.val >= val:
                count += 1
                compute(ro.left, ro.val)
                compute(ro.right, ro.val)
            else:
                compute(ro.left, val)
                compute(ro.right, val)

        compute(root, root.val)

        return count

