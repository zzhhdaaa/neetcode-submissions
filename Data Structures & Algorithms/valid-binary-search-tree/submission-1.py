# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque()
        queue.append([root, float('-inf'), float('inf')])

        while queue:
            curr, lbound, rbound = queue.pop()
            if curr is None:
                continue

            if not lbound < curr.val <rbound:
                return False
            
            queue.append([curr.left, lbound, curr.val])
            queue.append([curr.right, curr.val, rbound])
        
        return True
