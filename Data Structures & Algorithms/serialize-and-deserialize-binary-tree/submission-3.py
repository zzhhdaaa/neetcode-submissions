# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        queue = deque()
        queue.append(root)
        resList = []

        while queue:
            node = queue.popleft()
            if node is None:
                resList.append('N')
                continue
            resList.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        
        res = "_".join(resList)
        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "" or data[0] == 'N':
            return None
        
        values = data.split("_")
        root = TreeNode(values[0])

        queue = deque()
        queue.append(root)
        i = 1

        while i < len(values) and queue:
            node = queue.popleft()

            if i < len(values) and values[i] != 'N':
                left = TreeNode(int(values[i]))
                node.left = left
                queue.append(left)
            i += 1

            if i < len(values) and values[i] != "N":
                right = TreeNode(int(values[i]))
                node.right = right
                queue.append(right)
            i += 1
        
        return root
