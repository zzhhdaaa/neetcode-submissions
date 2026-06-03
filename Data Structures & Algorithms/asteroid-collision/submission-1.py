class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # head = Node(asteroids[0])
        # curr = head

        # # build doubly linked list
        # for i in range(1, len(asteroids)):
        #     node = Node(asteroids[i])
        #     node.left = curr
        #     curr.right = node
        #     curr = node
        
        # # perform the collision test
        # clean = False
        # while not clean:
        #     curr = head
        #     while node:
        #         if node.right and node.right.val * node.val < 0:
        #             # collision
        #             keep

        stack = []
        for ast in asteroids:
            # no collision
            if len(stack) == 0 or ast*stack[-1] > 0:
                stack.append(ast)
                continue
            
            # collision happens only when the incoming one is negative and the right most one is positive
            while len(stack) != 0 and stack[-1]>0 and ast<0:
                if abs(stack[-1]) > abs(ast):
                    ast = 0
                    break
                elif abs(stack[-1]) == abs(ast):
                    ast = 0
                    stack.pop()
                else:
                    stack.pop()
            
            # collision, ast state
            if ast != 0:
                stack.append(ast)
        
        return stack
        