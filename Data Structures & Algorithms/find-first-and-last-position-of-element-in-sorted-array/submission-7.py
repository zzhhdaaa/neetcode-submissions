class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # find starting
        l, r = 0, len(nums)-1
        while l<r:
            m = (l+r)//2

            if nums[m] >= target:
                r = m
            elif nums[m] < target:
                l = m + 1
            
        start = l if 0<=l<len(nums) and nums[l] == target else -1
        
        # find ending
        l, r = 0, len(nums)-1
        while l<r:
            m = (l+r)//2 + 1

            if nums[m] > target:
                r = m - 1
            elif nums[m] <= target:
                l = m
        
        end = l if 0<=l<len(nums) and nums[l] == target else -1
        
        return [start, end]