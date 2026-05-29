# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        head = ListNode()
        prev = None
        curr = head
        merging = True

        while merging:
            min_val = float('inf')
            min_idx = None
            all_none = True
            for i in range(len(lists)):
                node = lists[i]
                if node is None:
                    continue
                all_none = all_none and False
                if node.val < min_val:
                    min_val = node.val
                    min_idx = i
            if min_idx is None:
                merging = False
                if prev is not None:
                    prev.next = None
                break
            curr.val = min_val
            curr.next = ListNode()
            lists[min_idx] = lists[min_idx].next
            prev = curr
            curr = curr.next
        
        return head

            
                    