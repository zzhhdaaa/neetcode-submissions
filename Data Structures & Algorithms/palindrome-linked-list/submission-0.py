# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        last = None

        # find the middle and reverse the left part on the fly
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = last
            last = slow
            slow = temp
        
        # if only one item
        if last is None:
            return True
        
        # even end condition, fast is None, slow is at right
        # 1 1 1 1
        #     _
        #         _
        # odd end condition, fast is not None, slow is at middle
        # 1 1 1
        #   _
        #     _

        if fast:
            slow = slow.next
        
        while slow:
            if slow.val != last.val:
                return False
            slow = slow.next
            last = last.next
        
        return True