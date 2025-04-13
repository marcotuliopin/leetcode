from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def constructNumber(l: ListNode) -> int:
            it = l
            num = 0
            count = 1

            while it:
                num += it.val * count
                it = it.next
                count *= 10

            return num
        
        def constructList(n: int) -> ListNode:
            head = ListNode(n % 10)
            
            divisor = 100

            it = head
            while divisor // 10 < n:
                it.next = ListNode(n % divisor // (divisor // 10))
                it = it.next 
                divisor *= 10
            
            return head

        n1 = constructNumber(l1)
        n2 = constructNumber(l2)

        return constructList(n1 + n2)