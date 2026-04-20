class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = min(heights[left], heights[right]) * (right - left)

        # 1, 7, 2, 5, 4, 7, 3, 6
        # _                    _
        # 1 * 7
        # left is lower bound, we want to update it

        # 1, 7, 2, 5, 4, 7, 3, 6
        #    _                 _
        # 6 * 6
        # right is lower bound, we want to update it

        # 1, 7, 2, 5, 4, 7, 3, 6
        #    _              _   
        # 3 * 5
        # right is lower bound, we want to update it

        l = 0
        r = len(heights) - 1
        maxArea = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            maxArea = max(maxArea, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea
