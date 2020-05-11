# Time: O()     ms
# Memory: O()   MB
from typing import *

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def add(n1, n2, c):
            if (n1 == None and n2 == None) and c == 0:
                return None
            val1 = n1.val if n1 else 0
            val2 = n2.val if n2 else 0
            c = c if c else 0
            ans = val1 + val2 + c
            l = ListNode(ans % 10)
            next_c = ans // 10
            l.next = add(n1.next if n1 else None, n2.next if n2 else None, next_c)
            return l
        return add(l1, l2, 0)
