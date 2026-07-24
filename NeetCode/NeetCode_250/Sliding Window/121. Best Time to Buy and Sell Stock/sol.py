"""

The core insight

As you scan left to right, at each day you're really asking: "If I sell today, what's the best profit I could get, given the lowest price I've seen so far?"

you just need:

- The minimum price seen so far (best possible buy point up to now)
- The best profit achievable if I sold today = today's price - min_so_far
- Keep a running max of that profit across all days


"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = math.inf # tracks when we need to buy

        total_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                total_profit = max(profit, total_profit)
        
        return total_profit
    
# ------------------------- ------------------------- ------------------------

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        min_price = math.inf

        profit = 0

        for price in prices:
            min_price = min(min_price , price)
            cur_profit = price - min_price
            
            profit = max(profit, cur_profit)
        
        return profit