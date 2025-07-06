# Tc: O(n^2)
# Sc: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        max_profit = 0

        for i in range(n):
            purchase = prices[i]
            
            for j in range(i, n):
                sold = prices[j]

                cur_profit = sold - purchase

                max_profit = max(max_profit, cur_profit)
        
        return max_profit
