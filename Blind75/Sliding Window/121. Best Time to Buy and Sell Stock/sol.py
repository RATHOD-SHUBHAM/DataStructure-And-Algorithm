'''
    There is a profit only if
    selling price is more than purchased price

    so we look for smaller number  - If there exist any before the current day price where we sell.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        purchased_cost = prices[0]
        max_profit = 0

        for i in range(1, n):
            # Current price
            selling_price = prices[i]

            cur_profit = selling_price - purchased_cost

            max_profit = max(max_profit, cur_profit)

            # if cur price < purchased cost
            purchased_cost = min(purchased_cost , selling_price)
        
        return max_profit