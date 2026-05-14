class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [0] * len(nums)
        res = 1

        for i in range(len(nums)-1, -1, -1):
            maxLen = 1
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    maxLen = max(1 + LIS[j], maxLen)
            LIS[i] = maxLen
            res = max(res, maxLen)
        
        return res