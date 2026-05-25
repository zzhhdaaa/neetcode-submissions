class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        LEN = len(nums)

        # mark all negative values as 0
        for i in range(LEN):
            if nums[i] < 0:
                nums[i] = 0
        
        # check each value, and mark the value in their corresponding index as negative
        for i in range(LEN):
            val = abs(nums[i])
            idx = val - 1
            if 0<=idx<LEN:
                if nums[idx] == 0:
                    nums[idx] = -val
                else:
                    nums[idx] = -abs(nums[idx])
        
        # check for the first negative value and return
        for res in range(1,LEN+1):
            idx = res - 1
            if nums[idx] >= 0:
                return res
        
        return LEN+1
