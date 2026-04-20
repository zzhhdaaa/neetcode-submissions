class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -4, -1, -1, 0, 1, 2
        # __          _
        nums = sorted(nums)
        results = []

        for i in range(len(nums)-2):
            num = nums[i]

            if i>0 and nums[i] == nums[i-1]:
                continue

            # define the left and right bound
            left = i+1
            right = len(nums)-1
            
            while left < right:
                threeSum = num + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                elif threeSum == 0:
                    results.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        
        return results
                



