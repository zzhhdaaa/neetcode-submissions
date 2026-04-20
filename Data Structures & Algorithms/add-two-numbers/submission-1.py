# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 0  0  1  1
        # 1, 2, 3
        # 4, 9, 8
        # 5, 1, 2, 1

        addition = 0
        head = ListNode()
        curr = head
        next = None

        while l1 is not None or l2 is not None or addition != 0:
            summary = 0
            if l1 and l2:
                summary = l1.val + l2.val + addition
                l1 = l1.next
                l2 = l2.next
            elif l1 is None and l2 is None and addition != 0:
                summary = addition
            elif l1 is None:
                summary = l2.val + addition
                l2 = l2.next
            elif l2 is None:
                summary = l1.val + addition
                l1 = l1.next
            
            addition = summary // 10
            summary = summary % 10
            curr.val = summary
            
            if addition != 0 or l1 or l2:
                next = ListNode()
            else:
                next = None

            curr.next = next
            curr = next
        
        return head
