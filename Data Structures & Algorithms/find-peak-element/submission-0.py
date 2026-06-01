class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        LEN = len(nums)
        l = 0
        r = LEN - 1

        while l<r:
            m = (l+r)//2

            if (m+1>=LEN or nums[m]>nums[m+1]) and (m-1<0 or nums[m]>nums[m-1]):
                return m
            elif m-1<0 or nums[m]>=nums[m-1]:
                l = m+1
            else:
                r = m-1
        
        return l
                