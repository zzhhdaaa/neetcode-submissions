class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # 10,6,8,5,11,9
        #             ^
        #           ^
        #         

        res = [0] * len(heights)
        stack = [] # this is the reverse stack
        for i in range(len(heights)-1, -1, -1):
            # we use the existing stack info to determin how many ones can the new one see
            # if stack and stack[-1] < heights[i]:
            #     res[i] = len(stack)
            # elif stack:
            #     res[i] = 1
            # else:
            #     res[i] = 0

            count = 0
            # if the new one will block the old ones, remove the old ones before adding the new one
            while stack and stack[-1] < heights[i]:
                stack.pop()
                count += 1
            count += 1 if stack else 0
            stack.append(heights[i])
            res[i] = count
        
        return res
