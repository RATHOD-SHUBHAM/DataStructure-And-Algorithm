class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        profit = 0

        left = 0 # buy day
        right = 1 # Sell day

        while right < n:
            if prices[right] < prices[left]:
                left = right
            
            profit = max(prices[right] - prices[left], profit)

            right += 1
        
        return profit
    

# ----------------- Or ---------------------

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        left = 0

        max_profit = 0

        for right in range(1, n):
            # if current day price is lesser than previous day - then buy today
            if prices[right] < prices[left]:
                left = right
            
            cur_profit = prices[right] - prices[left]

            max_profit = max(max_profit, cur_profit)
        
        return max_profit