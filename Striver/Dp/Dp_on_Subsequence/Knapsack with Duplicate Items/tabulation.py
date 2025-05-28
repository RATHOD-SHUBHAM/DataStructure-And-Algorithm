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
