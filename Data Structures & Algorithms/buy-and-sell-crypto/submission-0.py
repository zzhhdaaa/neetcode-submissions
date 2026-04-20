class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0

        for i in range(1, len(prices)):
            if prices[i]-prices[left] > max_profit:
                max_profit = prices[i]-prices[left]
            if prices[i]-prices[left]<0:
                left = i
        
        return max_profit
