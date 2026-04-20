# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #  1
        # 2, 3
        #     4
        #      5

        flag = True
        
        def dfs(root: Optional[TreeNode], depth: int) -> int:
            if root is None:
                return depth
            else:
                depth += 1

            nonlocal flag
            
            lDepth = dfs(root.left, depth)
            rDepth = dfs(root.right, depth)

            if abs(lDepth-rDepth) > 1:
                flag = False
            
            return max(lDepth, rDepth)
        
        dfs(root, 0)
        return flag
