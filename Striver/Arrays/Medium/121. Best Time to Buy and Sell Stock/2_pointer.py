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