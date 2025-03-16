import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        c = 0

        for i in range(len(lists)):
            it = lists[i]
            while it:
                heapq.heappush(h, (it.val, c, it))
                it = it.next
                c += 1

        if not h:
            return None

        _, _, head = heapq.heappop(h)
        it = head
        while h:
            _, _, node = heapq.heappop(h)
            it.next = node
            it = it.next
        return head

