# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # for every node, the max is itself + max(its left max, its right max, zero)
        # basically what we're looking for is the max of all time

        maxSum = float('-inf')
        maxVal = float('-inf')
        def dfs(node: Optional[TreeNode]):
            nonlocal maxSum
            nonlocal maxVal
            if not node:
                # reach end
                return 0
            
            leftmax = dfs(node.left)
            rightmax = dfs(node.right)
            selfmax = max(node.val+leftmax+rightmax, 0) # used to update maxSum
            selfres = max(node.val+max(leftmax,rightmax), 0) # used to return for upper layer, couldn't take both if going up
            maxSum = max(maxSum, selfmax)
            maxVal = max(maxVal, node.val)
            return selfres
        
        dfs(root)
        if maxSum == 0 and maxVal < 0:
            return maxVal
        return maxSum