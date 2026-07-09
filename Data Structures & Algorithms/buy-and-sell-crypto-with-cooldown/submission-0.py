class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # decision tree:
        # holding ------- not holding
        # sell vs hold -- buy vs hold
        memo = dict()

        def dfs(i: int, holding: int) -> int:
            if i >= len(prices):
                return 0
            
            if (i, holding) in memo:
                return memo[(i, holding)]
            
            # keep it
            profit = dfs(i+1, holding)

            # sell it
            if holding != -1 and prices[i] > holding:
                profit = max(profit, prices[i] - holding + dfs(i+2, -1))

            # buy it
            if holding == -1:
                profit = max(profit, dfs(i+1, prices[i]))
            
            memo[(i, holding)] = profit
            return profit
        
        return dfs(0, -1)