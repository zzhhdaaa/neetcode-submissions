class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # ------- 1 / 1 two
        # ------ 1 / 1 one
        # ----- 1 / 2
        # ---- 2 / 3
        # --- 1 / 3
        # -- 2 / 5 <-
        # - 1 / 4 <- win

        one = cost[-2]
        two = cost[-1]

        if len(cost) == 2:
            return min(one, two)

        for i in range(len(cost)-2):
            temp = min(one, two) + cost[len(cost)-3-i]
            two = one
            one = temp
        
        return min(one, two)
