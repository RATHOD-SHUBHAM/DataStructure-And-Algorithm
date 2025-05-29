#User function Template for python3
import math

class Solution:
    def cutRod(self, price):
        n = W = len(price)
        
        Wi = [i for i in range(1, n+1)]
        
        Vi = price
        
        dp = [0 for _ in range(W+1)]
        
        # Base case
        for cur_weight in range(W+1):
            if Wi[0] <= cur_weight:
                remaining_capacity = cur_weight // Wi[0]
                dp[cur_weight] = remaining_capacity * Vi[0]
        
        # Logic
        for idx in range(1, n):
            temp = [0 for _ in range(W+1)]
            for cur_weight in range(W+1):
                
                if Wi[idx] <= cur_weight:
                    take = Vi[idx] + temp[cur_weight - Wi[idx]]
                else:
                    take = -math.inf
                
                no_take = 0 + dp[cur_weight]
                
                temp[cur_weight] = max(take, no_take)
            
            dp = temp
        
        return dp[W]
    
    