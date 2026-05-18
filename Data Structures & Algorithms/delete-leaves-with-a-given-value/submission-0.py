# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return None
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            return None if node.left is None and node.right is None and node.val == target else node
        
        return dfs(root)
