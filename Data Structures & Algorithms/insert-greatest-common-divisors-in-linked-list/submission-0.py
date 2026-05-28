# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # two parts:
        # 1. insert a node in between nodes
        # 2. find greatest common divisors

        def get_gcd(a: int, b: int) -> int:
            for i in range(min(a,b), 0, -1):
                if a%i == b%i == 0:
                    return i

        queue = deque()
        queue.append(head)

        while queue:
            node1 = queue.popleft()
            node2 = node1.next

            if node2 is None:
                break
            
            gcd = get_gcd(node1.val, node2.val)

            node_gcd = ListNode()
            node_gcd.val = gcd

            node1.next = node_gcd
            node_gcd.next = node2

            queue.append(node2)
        
        return head
