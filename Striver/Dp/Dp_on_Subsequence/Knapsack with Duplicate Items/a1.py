import math

class Solution:
    def knapSack(self, val, wt,capacity):
        # code here
        n = len(wt)

        idx = n - 1

        return self.recursion(idx, wt, val, capacity)
    
    def recursion(self, idx, wt, val, capacity):
        # base case
        if idx == 0:
            if wt[0] <= capacity:
                # Each item can be choosen infinite amount of time
                remaining_capacity = capacity // wt[0]
                return remaining_capacity * val[0]
            else:
                return 0
        
        # Logic
        if wt[idx] <= capacity:
            take = val[idx] + self.recursion(idx, wt, val, capacity - wt[idx])
        else:
            take = -math.inf

        no_take = 0 + self.recursion(idx - 1, wt, val, capacity )

        return max(take, no_take)

# ----------------------- Memoization -----------------------
#User function Template for python3
import math

class Solution:
    def knapSack(self, val, wt,capacity):
        # code here
        n = len(wt)

        idx = n - 1
        
        memo = {}

        return self.recursion(idx, memo, wt, val, capacity)
    
    def recursion(self, idx, memo, wt, val, capacity):
        # base case
        if idx == 0:
            if wt[0] <= capacity:
                # Each item can be choosen infinite amount of time
                remaining_capacity = capacity // wt[0]
                return remaining_capacity * val[0]
            else:
                return 0
        
        if (idx, capacity) in memo:
            return memo[(idx, capacity)]
        
        # Logic
        if wt[idx] <= capacity:
            take = val[idx] + self.recursion(idx, memo, wt, val, capacity - wt[idx])
        else:
            take = -math.inf

        no_take = 0 + self.recursion(idx - 1, memo, wt, val, capacity )

        memo[(idx, capacity)] = max(take, no_take)
        
        return memo[(idx, capacity)]

# -------------------------------- Tabulation  --------------------------------
#User function Template for python3
import math

class Solution:
    def knapSack(self, val, wt,capacity):
        n = len(wt)
        
        dp = [[0 for _ in range(capacity+1)]for _ in range(n)]

        # Base case
        for cur_weight in range(capacity+1):
            if wt[0] <= cur_weight:
                remaining_capacity = cur_weight // wt[0]
                dp[0][cur_weight] = remaining_capacity * val[0]
        
        # Logic
        for idx in range(1, n):
            for cur_weight in range(capacity+1):
                
                if wt[idx] <= cur_weight:
                    take = val[idx] + dp[idx][cur_weight - wt[idx]]
                else:
                    take = -math.inf

                no_take = 0 + dp[idx - 1][cur_weight]

                dp[idx][cur_weight] = max(take, no_take)

        return dp[n-1][capacity]

# -------------------------------- Space Optimization  --------------------------------
#User function Template for python3
import math

class Solution:
    def knapSack(self, val, wt,capacity):
        n = len(wt)
        
        dp = [0 for _ in range(capacity+1)]

        # Base case
        for cur_weight in range(capacity+1):
            if wt[0] <= cur_weight:
                remaining_capacity = cur_weight // wt[0]
                dp[cur_weight] = remaining_capacity * val[0]
        
        # Logic
        for idx in range(1, n):
            temp = [0 for _ in range(capacity+1)]
            for cur_weight in range(capacity+1):
                
                if wt[idx] <= cur_weight:
                    take = val[idx] + temp[cur_weight - wt[idx]]
                else:
                    take = -math.inf

                no_take = 0 + dp[cur_weight]

                temp[cur_weight] = max(take, no_take)
            
            dp = temp

        return dp[capacity]
