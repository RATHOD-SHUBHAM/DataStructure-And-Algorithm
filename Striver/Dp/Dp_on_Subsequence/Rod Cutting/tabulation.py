#User function Template for python3
import math

class Solution:
    def cutRod(self, price):
        n = len(price)
        
        Wi = []
        for i in range(1, n+1):
            Wi.append(i)
        
        return self.knapsack(Wi, Vi = price, W = n)
    
    def knapsack(self, Wi, Vi, W):
        
        n = W
        
        dp = [[0 for _ in range(W+1)] for _ in range(n)]
        
        # Base case
        for cur_weight in range(W+1):
            if Wi[0] <= cur_weight:
                remaining_capacity = cur_weight // Wi[0]
                dp[0][cur_weight] = remaining_capacity * Vi[0]
        
        # Logic
        for idx in range(1, n):
            for cur_weight in range(W+1):
                
                if Wi[idx] <= cur_weight:
                    take = Vi[idx] + dp[idx][cur_weight - Wi[idx]]
                else:
                    take = -math.inf
                
                no_take = 0 + dp[idx - 1][cur_weight]
                
                dp[idx][cur_weight] = max(take, no_take)
        
        return dp[n-1][W]
            
        