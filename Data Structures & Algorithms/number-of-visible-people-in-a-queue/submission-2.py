class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = [0] * len(heights)
        stack = [] # each one is height

        for i in range(len(heights)-1, -1, -1):
            height = heights[i]
            
            count = 0
            while stack and height >= stack[-1]:
                stack.pop()
                count += 1
            
            res[i] = count + 1 if stack else count
            stack.append(height)
        
        return res
                

