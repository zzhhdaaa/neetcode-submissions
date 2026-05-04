# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = None
        def dfs(node: Optional[TreeNode]):
            nonlocal lca

            if node is None:
                return 0
            if lca is not None:
                return 0
            
            count = 0
            if node.val == p.val or node.val == q.val:
                count += 1
            count += dfs(node.left) + dfs(node.right)

            if lca is None and count == 2:
                print("found")
                lca = node
            
            return count
        
        dfs(root)
        return lca