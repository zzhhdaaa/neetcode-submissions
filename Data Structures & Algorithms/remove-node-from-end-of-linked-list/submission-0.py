# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # <> <> <> <>
        # n = 2
        # length = 4
        # index = 2
        # we want to update 1's next to 3
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        curr = head
        index = length - n
        if index == 0:
            return curr.next
        for i in range(index):
            if i == index - 1:
                curr.next = None if curr.next is None else curr.next.next
            curr = curr.next
        
        return head

