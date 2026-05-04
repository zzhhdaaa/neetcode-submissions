# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        n = 0
        
        def dfs(node: Optional[TreeNode]):
            nonlocal res
            nonlocal n

            if node is None:
                return
            
            if n == k:
                return
            
            dfs(node.left)
            if n == k:
                return
            
            res = node.val
            n += 1
            if n == k:
                return
            
            dfs(node.right)
        
        dfs(root)
        return res
            