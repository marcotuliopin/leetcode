from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        it = head
        while it:
            # Copy current node without the random pointer.
            it.next = Node(it.val, it.next)

            if it.next.next is None:
                break

            it = it.next.next
        
        itog = head
        itcp = head.next

        while itog:
            # Copy random pointer.
            if itog.random:
                itcp.random = itog.random.next
            
            if itcp.next is None:
                break

            itog = head.next.next
            itcp = head.next.next
        
        # Unweave both lists.
        headcp = head.next
        itcp = headcp
        while itcp.next:
            itcp.next = itcp.next.next
            itcp = itcp.next

        return headcp
