"""
Look for every peak following a valley, 
and track the costs corresponding to the peaks and valleys along with the maximum profit
"""

# Tc: O(n)
# Sc: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        i = 0 
        total_profit = 0

        while i < n:
            # For every valley
            buy = prices[i]

            max_profit = 0
            j = i + 1

            # Capture the peak
            while j < n:
                # Check for peak
                if prices[j] > prices[j-1]:
                    profit = prices[j] - buy
                    
                    max_profit = max(max_profit, profit)

                    j += 1
                else:
                    # If there is a dip
                    break
            
            # Gather the profit
            total_profit += max_profit
            i = j

        return total_profit

# --------------------------------- Same logic with a different approach ---------------------------------
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        total_profit = 0

        i = 0

        while i < n: # Iterate for valley
            j = i + 1

            # Find the peak
            while j < n and prices[j] > prices[j-1]:
                j += 1
            
            profit = prices[j-1] - prices[i] # Sell - Buy
            total_profit += profit
            
            i = j # Move to the next valley
        
        return total_profit

        