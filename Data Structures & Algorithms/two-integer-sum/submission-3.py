class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = dict()
        for i in range(0, len(nums)):
            if nums[i] in ref.keys():
                return [ref[nums[i]], i]
            ref[target-nums[i]] = i
        
        return