# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # -    0 -> 1 -> 2 -> 3
        # p    c
        # - <- 0    1 -> 2 -> 3
        #      p    c
        # - <- 0 <- 1    2 -> 3
        #           p    c
        # ... ...
        # - <- 0 <- 1 <- 2 <- 3    -
        #                     p    c

        # iterative
        # prev = None
        # curr = head

        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        
        # return prev

        # recursive
        def reverse(prev: Optional[ListNode], curr: Optional[ListNode]) -> Optional[ListNode]:
            if curr is None:
                return prev
            
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

            return reverse(prev, curr)
        
        return reverse(None, head)
