class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # we only search through the idx 0, 2, 4, 6, ... len(nums)-1
        l = 0
        r = len(nums) // 2

        while l<=r:
            m = (l+r) // 2
            idx = m*2
            left = nums[idx-1] if idx-1>=0 else float('-inf')
            middle = nums[idx]
            right = nums[idx+1] if idx+1<len(nums) else float('inf')

            if left < middle < right:
                return middle
            elif left == middle:
                # in left portion
                r = m
            elif middle == right:
                # in right portion
                l = m+1

