"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        node_clone = Node()
        queue = deque()
        queue.append([node, node_clone]) # curr node, curr clone, last node
        seen = set()
        created = dict()
        created[node.val] = node_clone
        
        while queue:
            curr, curr_clone = queue.popleft()
            if curr in seen:
                continue
            seen.add(curr)
            curr_clone.val = curr.val
            for nei in curr.neighbors:
                if nei.val in created:
                    curr_clone.neighbors.append(created[nei.val])
                    continue
                nei_clone = Node()
                created[nei.val] = nei_clone
                curr_clone.neighbors.append(nei_clone)
                queue.append([nei, nei_clone])
        
        return node_clone

