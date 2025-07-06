"""
Instead of looking for every peak following a valley, 
we can simply go on crawling over the slope and keep on adding the profit obtained from every consecutive transaction. 
In the end,we will be using the peaks and valleys effectively, 
but we need not track the costs corresponding to the peaks and valleys along with the maximum profit, 
but we can directly keep on adding the difference between the consecutive numbers of the array if the second number is larger than the first one, and at the total sum we obtain will be the maximum profit.
"""

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