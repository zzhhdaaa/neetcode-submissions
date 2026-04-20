# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # -, 1, 2, 3
        # p  c

        def reverse(prev: Optional[ListNode], curr: Optional[ListNode]) -> Optional[ListNode]:
            if curr is None:
                return prev
            
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

            return reverse(prev, curr)
        
        def toNum(head: Optional[ListNode]) -> int:
            if head is None:
                return 0
            
            num = 0
            while head is not None:
                num = num * 10 + head.val
                head = head.next
            
            return num

        # 123
        # 3 -> 2 -> 1
        # p    c
        def toList(num: int) -> Optional[ListNode]:
            head = ListNode()
            if num == 0:
                return head

            head.val = num % 10
            num = num // 10
            prev = head
            curr = None
            while num != 0:
                curr = ListNode()
                curr.val = num % 10
                num = num // 10
                prev.next = curr
                prev = curr
            
            return head
        
        l1R = reverse(None, l1)
        l2R = reverse(None, l2)

        return toList(toNum(l1R) + toNum(l2R))
