# Tc: O(n)
# Sc: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        max_profit = 0

        min_price = prices[0]


        for i in range(1, n):
            cur_price = prices[i]

            if cur_price < min_price:
                min_price = cur_price
            else:
                cur_profit = cur_price - min_price
                max_profit = max(max_profit , cur_profit)
        
        return max_profit
