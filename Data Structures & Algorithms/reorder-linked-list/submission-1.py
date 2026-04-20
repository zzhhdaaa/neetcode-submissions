# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def invert(head: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            curr = head

            while curr is not None:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

            return prev
        
        fast = head
        slow = head

        while fast is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
            temp = slow.next
            if fast is None:
                slow.next = None
            slow = temp
        
        list1 = head
        list2 = invert(slow)

        while list1 and list2:
            temp1 = list1.next
            temp2 = list2.next
            list1.next = list2
            list2.next = temp1
            list1 = temp1
            list2 = temp2

        return


