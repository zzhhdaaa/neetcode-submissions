# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i = 1
        curr = head
        leftside = None

        # prepare for the left part
        while i < left:
            leftside = curr
            curr = curr.next
            i += 1
        
        start = curr
        prev = None
        # start reversing, from left to right
        while i <= right:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            i += 1
        
        # now, i == right+1
        # curr is the rightside connector
        # leftside connector needs to connect to the prev
        # start needs to connect to the rightside connector
        start.next = curr
        if leftside is None:
            return prev
        
        leftside.next = prev
        return head


        