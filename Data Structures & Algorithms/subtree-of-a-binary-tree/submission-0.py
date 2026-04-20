# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None and q is None:
                return True

            if (p is None and q is not None) or \
                (q is None and p is not None) or \
                p.val != q.val:
                return False
            
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        flag = False
        def dfs(root: Optional[TreeNode]):
            nonlocal subRoot
            nonlocal flag

            if root is None:
                if subRoot is None:
                    flag = True
                return

            if isSameTree(root, subRoot):
                flag = True
                return
            
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return flag
