class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -4,-1,-1, 0, 1, 2
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i != 0 and nums[i-1] == nums[i]:
                continue
            target = 0 - nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                summary = nums[left] + nums[right]
                if summary == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < len(nums) - 1 and nums[left] == nums[left-1]:
                        left += 1
                elif summary > target:
                    right -= 1
                elif summary < target:
                    left += 1
        
        return res