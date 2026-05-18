class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3 # the count of 0, 1, 2

        for num in nums:
            count[num] += 1
        
        for i in range(len(nums)):
            if count[0] != 0:
                nums[i] = 0
                count[0] -= 1
            elif count[1] != 0:
                nums[i] = 1
                count[1] -= 1
            elif count[2] != 0:
                nums[i] = 2
                count[2] -= 1
        
