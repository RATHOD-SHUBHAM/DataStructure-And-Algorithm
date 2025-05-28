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
