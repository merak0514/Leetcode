# Time: O()     ms
# Memory: O()   MB
from typing import *
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        target = ListNode(None)
        start = []
        new_list = []
        for li in lists:
            if li:
                start.append(li.val)
                new_list.append(li.next)
        heap = heapq.heapify(start)
        while True:
            heapq.heappushpop()
        return target
