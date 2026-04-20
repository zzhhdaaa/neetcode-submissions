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

        while l1 or l2 or addition != 0:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            summary = v1 + v2 + addition
            
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
