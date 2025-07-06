# Tc: O(n)
# Sc: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        total_profit = 0

        for i in range(1, n):
            # If price goes up, capture the profit
            if prices[i] > prices[i-1]:
                profit = prices[i] - prices[i-1]
                total_profit += profit
        
        return total_profit