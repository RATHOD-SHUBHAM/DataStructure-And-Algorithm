# ---------------------- Recursive Solution ----------------------

import math
#User function Template for python3
class Solution:
    def minCost(self, height):
        n = len(height)
        # 0 based index - hence n-1 will be the last index
        return self.recursion(n-1, height)
    
    def recursion(self, n, arr):
        if n == 0:
            # Cost it takes to jump from 0 to 0 step will be zero.
            return 0
        
        '''
        Cost it take to jump from 0 to n-1 index
        +
        Cost it takes to jump from n-1 to n index
        '''
        if n-1 >= 0:
            cost_jump_1 = self.recursion(n-1, arr) + abs(arr[n] - arr[n-1])
        else:
            cost_jump_1 = math.inf
        
        '''
        Cost it take to jump from 0 to n-2 index
        +
        Cost it takes to jump from n-2 to n index
        '''
        if n-2 >= 0:
            cost_jump_2 = self.recursion(n-2, arr) + abs(arr[n] - arr[n-2])
        else:
            cost_jump_2 = math.inf
        
        return min(cost_jump_1, cost_jump_2)
    

# --------------------- Memoization Solution ---------------------

import math
#User function Template for python3
class Solution:
    def minCost(self, height):
        n = len(height)
        dp = [-1] * (n)
        # 0 based index - hence n-1 will be the last index
        return self.memo(dp, n-1, height)
        
    
    def memo(self, dp, n, arr):
        if n == 0:
            # Cost it takes to jump from 0 to 0 step will be zero.
            return 0
        
        if dp[n] != -1:
            return dp[n]
        
        '''
        Cost it take to jump from 0 to n-1 index
        +
        Cost it takes to jump from n-1 to n index
        '''
        if n-1 >= 0:
            cost_jump_1 = self.memo(dp, n-1, arr) + abs(arr[n] - arr[n-1])
        else:
            cost_jump_1 = math.inf
        
        '''
        Cost it take to jump from 0 to n-2 index
        +
        Cost it takes to jump from n-2 to n index
        '''
        if n-2 >= 0:
            cost_jump_2 = self.memo(dp, n-2, arr) + abs(arr[n] - arr[n-2])
        else:
            cost_jump_2 = math.inf
        
        dp[n] = min(cost_jump_1, cost_jump_2)
        
        return dp[n]
    
# --------------------- Tabulation Solution ---------------------
import math
#User function Template for python3
class Solution:
    def minCost(self, height):
        n = len(height)
        
        # Base case
        if n < 2:
            return 0
            
        dp = [-1] * (n) # hold the minimum cost
        
        dp[0] = 0
        dp[1] = abs(height[0] - height[1])
        
        for i in range(2, n):
            cost_jump_1 = dp[i-1] + abs(height[i] - height[i-1])
            cost_jump_2 = dp[i-2] + abs(height[i] - height[i-2])
            
            dp[i] = min(cost_jump_1, cost_jump_2)
        
        return dp[n-1]
    
# --------------------- Space Optimized Solution ---------------------
import math
#User function Template for python3
class Solution:
    def minCost(self, height):
        n = len(height)
        
        # Base case
        if n < 2:
            return 0
        
        p_prev = 0 # Cost of jump at 0th step
        prev = abs(height[0] - height[1]) # cost of jump to 1st step
        
        for i in range(2, n):
            cost_jump_1 = prev + abs(height[i] - height[i-1])
            cost_jump_2 = p_prev + abs(height[i] - height[i-2])
            
            cur_cost = min(cost_jump_1, cost_jump_2)
            # Adjust index
            p_prev = prev
            prev = cur_cost
        
        return cur_cost