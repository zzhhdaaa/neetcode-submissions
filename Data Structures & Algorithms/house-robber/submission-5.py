class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1, 1, 3, 3
        # _
        #       _
        # _        _
        #    _     _
        #       _

        # at each house, rob vs no rob decision

        # money before the last one
        prev1 = 0
        # money including the last one
        prev2 = 0

        for num in nums:
            current = max(prev1 + num, prev2)
            prev1 = prev2
            prev2 = current
        
        return prev2