#User function Template for python3
import math

class Solution:
    def cutRod(self, price):
        n = len(price)
        
        Wi = []
        for i in range(1, n+1):
            Wi.append(i)
        
        
        idx = n - 1
        
        memo = {}
        
        return self.knapsack(idx, memo, Wi, Vi = price, W = n)
    
    def knapsack(self, idx, memo, Wi, Vi, W):
        # base case
        if idx == 0:
            if Wi[0] <= W:
                return (W // Wi[0]) * Vi[0]
            else:
                return 0
        
        if (idx, W) in memo:
            return memo[(idx, W)]
        
        # Logic
        if Wi[idx] <= W:
            take = Vi[idx] + self.knapsack(idx, memo, Wi, Vi, W - Wi[idx])
        else:
            take = -math.inf
        
        no_take = 0 + self.knapsack(idx - 1, memo, Wi, Vi, W)
        
        memo[(idx, W)] = max(take, no_take)
        
        return memo[(idx, W)]
        