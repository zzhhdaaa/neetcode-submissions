# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        
        curr = root

        while curr:
            # should go left
            if val < curr.val:
                if curr.left:
                    curr = curr.left
                    continue
                node = TreeNode(val)
                curr.left = node
                break
            elif val > curr.val:
                if curr.right:
                    curr = curr.right
                    continue
                node = TreeNode(val)
                curr.right = node
                break
        
        return root