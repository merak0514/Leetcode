# Time: O(m+n)     28ms
# Memory: O(m+n)   13.9MB
from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(None)
        p_l3 = l3
        while l1 or l2:
            if l1 and (not l2 or l1.val < l2.val):
                l3.next = ListNode(l1.val)
                l1 = l1.next
                l3 = l3.next
            else:
                l3.next = ListNode(l2.val)
                l2 = l2.next
                l3 = l3.next

        return p_l3.next
