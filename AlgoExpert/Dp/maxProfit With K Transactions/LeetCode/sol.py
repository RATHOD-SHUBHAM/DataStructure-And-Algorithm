# Time = O(nk)
# Space = O(n)
import math
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0 or k == 0:
            return 0
        
        # creating dp
        even = [0 for _ in range(len(prices))]
        odd = [0 for _ in range(len(prices))]
        
        
        for i in range(1, k+1):
            maxProfit = -math.inf
            
            if i % 2 == 0:
                cur = even
                prev = odd
            else:
                cur = odd
                prev = even
            
            # got throught prices
            for j in range(1, len(prices)):
                maxProfit = max(maxProfit, -prices[j-1] + prev[j-1])
                cur[j] = max(cur[j-1] , prices[j] + maxProfit)
                
        return even[-1] if k % 2 == 0 else odd[-1]