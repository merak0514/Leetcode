# Time: O(n)     88ms
# Memory: O(n)   12.8MB
from typing import *
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = 0
        n2 = 0
        p1 = l1
        p2 = l2

        while True:  # summation
            n1 += 1
            n2 += 1
            if p1.next == None:
                if p2.next == None:
                    break
                else:
                    n2 += 1
                    p2 = p2.next
            elif p2.next == None:
                n1 += 1
                p1 = p1.next
            else:
                n1 += 1
                n2 += 1
                p1 = p1.next
                p2 = p2.next

        del p1, p2

        if n1 < n2:  # ensure l1 > l2
            new_l1 = l2
            l2 = l1
            l1 = new_l1

            new_n1 = n2
            n2 = n1
            n1 = new_n1
        new = ListNode(0)
        p = new
        p1 = l1
        for _ in range(n1 - n2):
            p.next = ListNode(p1.val)
            p = p.next
            p1 = p1.next

        def add(node1, node2, pointer):
            if not node1:
                return 0
            pointer.next = ListNode(0)
            ans = node1.val + node2.val + add(node1.next, node2.next, pointer.next)  # recursion
            pointer.next.val = ans % 10
            c = ans // 10
            return c

        def add_carry(node):
            if node == p:
                ans = node.val + add(p1, l2, p)
                node.val = ans % 10
                return ans // 10
            ans = node.val + add_carry(node.next)
            node.val = ans % 10
            return ans // 10

        add_carry(new)
        return new.next if new.val == 0 else new  # normal case new.next; but if carry
