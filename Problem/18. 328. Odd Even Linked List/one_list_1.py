# Time: O(n)     56ms      11.3%
# Memory: O(1)   16MB      8.3%
from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        Initialize like below:
        a -> b -> c -> d -> e -> f
        p   l,r   n    h
        Algorithm:

        let p.next = n,
        n.next = l,
        r.next = h,
        then renew p,l,r,n,h.
        """

        if not head:                    # return if length == 0
            return head
        p = head  # previous
        if head.next:
            l = head.next  # left
        else:                           # return if length == 1
            return head
        r = l  # right
        if l.next:
            n = l.next  # next
        else:                           # length == 2
            return head
        if n.next:
            h = n.next
        else:                           # length == 3
            p.next = n
            n.next = l
            r.next = None
            return head
        while True:                     # length >= 4
            p.next = n
            n.next = l
            r.next = h
            if not h:
                break
            p = p.next
            r = h
            n = r.next
            if not n:
                break
            h = n.next
        return head

