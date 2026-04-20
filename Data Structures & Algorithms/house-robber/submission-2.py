class Solution:
    def rob(self, nums: List[int]) -> int:
        # - 2 / 16
        # -- 9 / 15
        # --- 8 / 14
        # ---- 3 / 6 one flag = True
        # ----- 6 / 6 two

        # when do we wanna add one:
        # 1. when one is greater, 2. when the index at one is not used
        # when do we wanna add two:
        # 2. when two is greater

        # we will actually always add two

        if len(nums) == 1:
            return nums[0]
        
        flag = nums[-2] > nums[-1]
        one = nums[-2] if flag else nums[-1]
        two = nums[-1]

        if len(nums) == 2:
            return one if flag else two

        for i in range(len(nums)-3, -1, -1):
            temp = one if one > two + nums[i] else two + nums[i]
            two = one
            one = temp
        
        return max(one, two)
