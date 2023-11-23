class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_profit = -math.inf
        boughtPrice = math.inf

        n = len(prices)

        for i in range(n):
            curPrice = prices[i]

            # if current price is lower than bought price - this will be the new price where we buy
            if curPrice < boughtPrice:
                boughtPrice = curPrice
            
            profit = curPrice - boughtPrice

            max_profit = max(max_profit, profit)
        
        return max_profit