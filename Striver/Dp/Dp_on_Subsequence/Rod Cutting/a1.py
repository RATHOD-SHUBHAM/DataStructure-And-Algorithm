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
        
# -# -------------------------------- Memoization  --------------------------------
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
        
# -# -------------------------------- Tabulation  --------------------------------
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
            
        
# -# -------------------------------- Space Optimization  --------------------------------
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
    
    