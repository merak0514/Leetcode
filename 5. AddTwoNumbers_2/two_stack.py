# Time: O(n)     68ms
# Memory: O(n)   12.8MB
from typing import *

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        p1 = l1
        p2 = l2
        while p1:
            stack1.append(p1.val)
            p1 = p1.next
        while p2:
            stack2.append(p2.val)
            p2 = p2.next
        head = ListNode(0)
        c = 0
        while stack1 or stack2:
            v1 = stack1.pop() if stack1 else 0
            v2 = stack2.pop() if stack2 else 0
            ans = v1 + v2 + c
            head.val = ans % 10
            c = ans // 10
            new = ListNode(0)
            new.next = head
            head = new
        if c == 1:
            head.val = 1
            return head
        else:
            return head.next
