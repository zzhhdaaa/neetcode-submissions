# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # maxLength(node) -> int
        #    node(max(0,2))
        #       node(max(2,1))
        #     node(1)    node(0)
        #   node(0)
        diameter = 0
        def maxDepth(node: Optional[TreeNode]) -> int:
            nonlocal diameter
            left = 0
            right = 0
            if node.left:
                left = 1 + maxDepth(node.left)
            if node.right:
                right = 1 + maxDepth(node.right)
            diameter = max(diameter, left+right)
            return max(left, right)
        
        maxDepth(root)
        return diameter
        
