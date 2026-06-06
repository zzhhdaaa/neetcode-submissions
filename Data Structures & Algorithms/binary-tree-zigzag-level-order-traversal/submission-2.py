# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque() # for even rows, append left, popleft
        re_queue = deque() # for odd rows, append right, pop

        queue.append(root)
        level = 0
        res = []
        curr = []

        while queue or re_queue:
            if level%2 == 0:
                node = queue.popleft()
                if node:
                    re_queue.appendleft(node.left)
                    re_queue.appendleft(node.right)
                    curr.append(node.val)
                if not queue:
                    # level ends
                    if len(curr) == 0:
                        continue
                    res.append(curr.copy())
                    curr = []
                    level += 1
            else:
                node = re_queue.popleft()
                if node:
                    queue.appendleft(node.right)
                    queue.appendleft(node.left)
                    curr.append(node.val)
                if not re_queue:
                    # level ends
                    if len(curr) == 0:
                        continue
                    res.append(curr.copy())
                    curr = []
                    level += 1
        
        return res
