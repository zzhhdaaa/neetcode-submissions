class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 2,-3,4,-2,2,1,-1,4

        maxsum = nums[0]
        cursum = 0

        for n in nums:
            if cursum < 0:
                cursum = 0
            cursum += n
            maxsum = max(cursum, maxsum)
        
        return maxsum