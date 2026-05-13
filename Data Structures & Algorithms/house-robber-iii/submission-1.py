# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = dict()

        def dfs(node: Optional[TreeNode], prevRobbed: bool):
            if node is None:
                return 0
            
            if (node,prevRobbed) in memo:
                return memo[(node,prevRobbed)]
            
            # rob this
            robThis = 0
            if not prevRobbed:
                robThis = node.val + dfs(node.left, True) + dfs(node.right, True)
            # skip this
            skipThis = dfs(node.left, False) + dfs(node.right, False)
            memo[(node,prevRobbed)] = max(robThis, skipThis)
            return memo[(node,prevRobbed)]
        
        return dfs(root, False)