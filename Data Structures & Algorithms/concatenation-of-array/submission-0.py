class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums.copy()

        for i in range(0, len(nums)):
            ans.append(nums[i])
        
        return ans
