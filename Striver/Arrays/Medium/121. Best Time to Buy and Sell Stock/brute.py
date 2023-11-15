# Tc: O(n) | Sc: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        buyDay = min(prices)
        idx_buyDay = prices.index(buyDay)

        print(buyDay, idx_buyDay)

        sellDay = -math.inf
        for i in range(idx_buyDay, n):
            cur_num = prices[i]

            if cur_num > sellDay:
                sellDay = cur_num
        
        return sellDay - buyDay