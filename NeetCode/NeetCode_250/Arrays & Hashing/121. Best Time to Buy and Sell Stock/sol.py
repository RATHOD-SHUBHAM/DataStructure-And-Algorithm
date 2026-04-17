"""
Idea:
Assume the current day is min price and explore the upcoming days in hope of finding a higher price to sell at. 

"""

# Tc: O(n^2) "|" Sc: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        profit = 0

        for i in range(n-1):
            min_price = prices[i] # assume current day price to be min
            
            # Explore to find high selling price
            for j in range(i+1, n):
                max_price = prices[j]

                cur_profit = max_price - min_price

                profit = max(profit, cur_profit)
        
        return profit

# ------------------------------------ Using 1 pass ------------------------------------

# Tc: O(n) "|" Sc: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        min_price = math.inf

        profit = 0

        for i in range(n):
            cur_price = prices[i]

            # If cur day has lower price then -> Buy
            if cur_price < min_price:
                min_price = cur_price # Valley
            
            else:
                # Sell on this day -> check the profit
                cur_profit = cur_price - min_price # Peak
                profit = max(profit, cur_profit) # Max Peak
        
        return profit


