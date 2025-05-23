#User function Template for python3
class Solution:
    def perfectSum(self, arr, target):
        # code he
        n = len(arr)
        
        dp = [0 for _ in range(target + 1)]
            
        if arr[0] == 0:
            dp[0] = 2
        else:
            dp[0] = 1
            if arr[0] < target + 1:
                dp[arr[0]] = 1
                
        
        for idx in range(1, n):
            temp = [0 for _ in range(target + 1)]
            for cur_sum in range(target + 1):
                if cur_sum >= arr[idx]:
                    take = dp[cur_sum - arr[idx]]
                else:
                    take = 0
                    
                no_take = dp[cur_sum]
                
                temp[cur_sum] = take + no_take
            
            dp = temp
            """
            Dont do dp[0] = 0
            
            In 2D DP:
            dp[i][0] = 1 means "using the first i elements, there's 1 way to get sum 0"
            This is the base case initialization - we set it once at the beginning
            But as we fill the table, when we encounter zeros, dp[i][0] can become 2, 4, 8, etc.
            
            In 1D DP (space optimized):
            dp[0] represents the current count of ways to achieve sum 0
            It starts at 1, but should grow as we process zeros in the array
            The key insight: we shouldn't reset it to 1 after each iteration
            """
            
        return dp[target]
        