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