# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root: Optional[TreeNode]) -> Optional[TreeNode]:
            if root is None or \
                (root.left is None and root.right is None):
                return root
            
            temp = invert(root.left)
            root.left = invert(root.right)
            root.right = temp
            return root

        return invert(root)