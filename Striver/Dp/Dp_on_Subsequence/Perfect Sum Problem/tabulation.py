#User function Template for python3
class Solution:
    def perfectSum(self, arr, target):
        # code here
        n = len(arr)
        
        # dp[i][j] will store the count of subsets from arr[0...i] with sum j
        dp = [[0 for _ in range(target + 1)] for _ in range(n)]
        
        # Base case:
        # Handle first element properly
        if arr[0] == 0:
            # If first element is 0, there are 2 ways to get sum 0:
            # 1. Don't take it (already counted in base case)
            # 2. Take it (still sum 0)
            dp[0][0] = 2  # Both ways lead to sum 0
        else:
            # If first element is non-zero, we can only form sum 0 by not taking it
            dp[0][0] = 1
            # First element is non-zero, then it can only contribute to its own value
            if arr[0] <= target:
                dp[0][arr[0]] = 1
        
        # Build up the dp table
        for idx in range(1, n):
            for cur_sum in range(target + 1):
                if cur_sum >= arr[idx]:
                    take = dp[idx - 1][cur_sum - arr[idx]]
                else:
                    take = 0
                
                no_take = dp[idx - 1][cur_sum]
                
                dp[idx][cur_sum] = take + no_take
        
        # Dp table tell user the count of subsets with sum equal to target
        return dp[n-1][target]
    