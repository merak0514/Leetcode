# Time: O(n)     40ms      85%
# Memory: O(1)   15.8MB      8%
from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        Step 1
        ------------------------
        a -> b -> c -> d -> e
        oe eh,et
        ========================
        Step 2
        ------------------------
        a -> c
            oe
        b -> d -> e
        eh   et
        ========================
        Step 3
        ------------------------
        a -> c -> e
                 oe
        b -> d -> Null
        eh         et
        ========================
        Step 4:
        Connect eh to oe.next
        ========================

        What is the difference between the previous one and this one?
        This method only do Step 4 ONCE (after reaching a Null at the end). So it use the same space as the previous
        one, but keeps two linked list.
        """
        if not head:
            return head
        odd_end = head
        even_head = head.next
        even_tail = even_head
        while even_tail and even_tail.next:
            odd_end.next = even_tail.next
            odd_end = odd_end.next
            even_tail.next = odd_end.next
            even_tail = even_tail.next
        odd_end.next = even_head
        return head

