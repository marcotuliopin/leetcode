from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(0, head)

        # Sort rest
        prev = dummy
        current = head
        while current:
            it = dummy
            while it != current:
                if not it.next or current.val < it.next.val:
                    prev.next = current.next
                    current.next = it.next
                    it.next = current
                    current = prev
                    break

                it = it.next

            prev = current
            current = current.next

        return dummy.next