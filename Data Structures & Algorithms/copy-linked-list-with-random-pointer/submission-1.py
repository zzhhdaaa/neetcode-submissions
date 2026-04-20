"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # loop through all the nodes, and make a copy
        # in the first loop, we don't link nodes yet
        # instead, we map the new node to the old node

        nodes = dict()

        curr = head
        while curr is not None:
            node = Node(curr.val)
            nodes[curr] = node
            curr = curr.next
        
        curr = head
        while curr is not None:
            nodes[curr].next = None if curr.next is None else nodes[curr.next]
            nodes[curr].random = None if curr.random is None else nodes[curr.random]
            curr = curr.next
        
        return None if head is None else nodes[head]
        