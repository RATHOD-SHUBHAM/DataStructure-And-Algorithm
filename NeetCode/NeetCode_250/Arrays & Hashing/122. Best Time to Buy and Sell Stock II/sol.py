"""
Total Profit=∑_i(height(peak_i)−height(valley_i​)

Idea: Every valley we buy stock and every peak we sell the stock
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        profit = 0

        i = 0

        while i < n - 1:
            # Get the next valley
            while i < n - 1 and prices[i] >= prices[i+1]:
                i += 1
            
            valley = prices[i]

            # Get the next peak
            while i < n - 1 and prices[i] <= prices[i+1]:
                i += 1
            
            peak = prices[i]

            cur_profit = peak - valley

            profit += cur_profit

        return profit
    

# ------------------------------------ Using 1 pass ------------------------------------

"""
Total Profit=∑_i(height(peak_i)−height(valley_i​)

Idea: Every inclination is a profit

Take ex :- [1,4,7,8]
if you take (1, 8) , diff = 7
or if you take (1, 4), (4, 7), (7, 8), diff = 3 + 3 + 1 = 7

Going directly to 8, or going to 8 by adding all differences in between is same in result, so rather than thinking to jump, think it in this way.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        profit = 0

        for i in range(1, n):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        
        return profit
