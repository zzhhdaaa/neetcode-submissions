class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 2 1 5 1 5 3
        # _
        #         _

        left = 0
        right = 0 # the actual window is nums[left:right+1] (right inclusive)
        total = 0
        res = float('inf')

        while right <= len(nums):
            if total >= target:
                res = min(res, right-left)
                total -= nums[left]
                left += 1
            elif total < target:
                if right < len(nums):
                    total += nums[right]
                right += 1
        
        return res if res != float('inf') else 0
