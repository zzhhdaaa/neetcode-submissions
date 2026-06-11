# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        tail = head
        LEN = 1
        while tail.next:
            LEN += 1
            tail = tail.next
        
        SHIFT = (LEN-k%LEN)%LEN
        for i in range(SHIFT):
            tmp = head
            head = head.next
            tmp.next = None
            tail.next = tmp
            tail = tmp
        
        return head