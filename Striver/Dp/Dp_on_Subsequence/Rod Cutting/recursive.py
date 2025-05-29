#User function Template for python3
import math

class Solution:
    def cutRod(self, price):
        n = len(price)
        
        Wi = []
        for i in range(1, n+1):
            Wi.append(i)
        
        
        idx = n - 1
        
        return self.knapsack(idx, Wi, Vi = price, W = n)
    
    def knapsack(self, idx, Wi, Vi, W):
        # base case
        if idx == 0:
            if Wi[0] <= W:
                return (W // Wi[0]) * Vi[0]
            else:
                return 0
        
        # Logic
        if Wi[idx] <= W:
            take = Vi[idx] + self.knapsack(idx, Wi, Vi, W - Wi[idx])
        else:
            take = -math.inf
        
        no_take = 0 + self.knapsack(idx - 1, Wi, Vi, W)
        
        return max(take, no_take)
        