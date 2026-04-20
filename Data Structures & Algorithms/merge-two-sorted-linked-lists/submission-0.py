# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        curr1 = list1
        curr2 = list2
        head = None
        curr = None

        if curr1.val <= curr2.val:
            head = curr1
            curr = curr1
            curr1 = curr1.next
        else:
            head = curr2
            curr = curr2
            curr2 = curr2.next

        while curr:
            if curr2 is None or (curr1 is not None and curr1.val <= curr2.val):
                curr.next = curr1
                curr = curr1
                curr1 = curr1.next if curr1 is not None else None
            elif curr1 is None or (curr2 is not None and curr1.val > curr2.val):
                curr.next = curr2
                curr = curr2
                curr2 = curr2.next if curr2 is not None else None
        
        return head


        