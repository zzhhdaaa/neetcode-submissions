class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = dict()
        for i in range(len(nums)):
            if nums[i] not in ref.keys():
                ref[target - nums[i]] = i
            else:
                return [ref[nums[i]], i]