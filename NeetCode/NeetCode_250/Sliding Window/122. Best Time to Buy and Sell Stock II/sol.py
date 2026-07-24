class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        i = 0

        total_profit = 0

        while i < n - 1:
            # Get the valley : buy
            while i < n-1 and prices[i] >= prices[i+1]:
                i += 1
            
            valley = prices[i]


            # get the peak: sell
            while i < n - 1 and prices[i] <= prices[i+1]:
                i += 1
            
            peak = prices[i]

            profit = peak - valley

            total_profit += profit
        
        return total_profit

            
