class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # 1,1,1,0,0,0,1,1,1,1,0
        # _
        # _

        l, r = 0, 0
        count = dict()
        count[0] = 0
        count[1] = 0

        res = 0
        while r < len(nums):
            # take r
            count[nums[r]] += 1

            # count validation
            if k < count[0]:
                # move l if invalid
                count[nums[l]] -= 1
                l += 1

            # move r
            r += 1
            res = max(res, r-l)
        
        return res