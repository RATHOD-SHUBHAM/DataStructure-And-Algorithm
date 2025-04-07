# --------------------------- Recursion ---------------------------

import math

#User function Template for python3
class Solution:
    def minimizeCost(self, k, arr):
        n = len(arr)
        # Since the arr is 0 based index, the last element will be at position n-1
        return self.recursion(n-1, k, arr)
        
    def recursion(self, n, k, arr):
        # base case
        if n == 0:
            return 0
        
        min_cost = math.inf
        for i in range(1, k+1):
            if n - i < 0:
                break
            
            
            cur_cost = self.recursion(n-i, k, arr) + abs(arr[n] - arr[n-i])
        
            
            min_cost = min(min_cost, cur_cost)
        
        return min_cost

# ------------------- Memoization -------------------
import math
#User function Template for python3
class Solution:
    def minimizeCost(self, k, arr):
        n = len(arr)
        dp = [-1] * (n)
        
        return self.memo(dp, n-1, k, arr)
    
    def memo(self, dp, n, k, arr):
        if n == 0:
            return 0
        
        if dp[n] != -1:
            return dp[n]
        
        min_cost = math.inf
        for i in range(1, k+1):
            if n - i < 0:
                break
            cur_cost = self.memo(dp, n-i, k, arr) + abs(arr[n] - arr[n-i])
            min_cost = min(cur_cost, min_cost)
        
        dp[n] = min_cost
        return dp[n]

# ------------------- Tabulation -------------------
import math
#User function Template for python3
class Solution:
    def minimizeCost(self, k, arr):
        n = len(arr)
        dp = [-1] * (n)
        
        dp[0] = 0
        
        for idx in range(1, n):
            min_cost = math.inf
            for j in range(1, k+1):
                if idx - j < 0:
                    break
                
                cur_cost = dp[idx - j] + abs(arr[idx] - arr[idx - j])
                min_cost = min(cur_cost, min_cost)
            
            dp[idx] = min_cost
        
        return dp[n-1]