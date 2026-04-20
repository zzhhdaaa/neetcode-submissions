class Solution:
    def climbStairs(self, n: int) -> int:
        # n = 5
        # ----- 1
        # ---- 1
        # --- 2
        # -- 3
        # - 5
        # 8
        oneStep = 1
        twoStep = 1
        for i in range(n-1):
            temp = oneStep + twoStep
            twoStep = oneStep
            oneStep = temp
        
        return oneStep