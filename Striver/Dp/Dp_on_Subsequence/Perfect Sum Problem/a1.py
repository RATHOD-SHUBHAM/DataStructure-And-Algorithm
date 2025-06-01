
#User function Template for python3
class Solution:
    def perfectSum(self, arr, target):
        # code he
        n = len(arr)
        
        idx = n - 1
        
        return self.recursion(idx, n, arr, target)

    def recursion(self, idx, n, arr, target):
        # base case
        if idx < 0:
            if target == 0:
                return 1
            else:
                return 0

        # Logic
        if target >= arr[idx]:
            take = self.recursion(idx - 1, n, arr, target - arr[idx])
        else:
            take = 0
            
        no_take = self.recursion(idx - 1, n, arr, target)
        
        return take + no_take
    
# --------------------------- Memoization ---------------------------

#User function Template for python3
class Solution:
    def perfectSum(self, arr, target):
        # code here
        n = len(arr)
        
        idx = n - 1
        
        memo = {}
        
        return self.recursion(idx, memo, arr, target)
        

    def recursion(self, idx, memo, arr, target):
        # base case
        if idx < 0:
            if target == 0:
                return 1
            else:
                return 0
                
        if (idx, target) in memo:
            return memo[(idx, target)]
                
        if arr[idx] <= target:
            take = self.recursion(idx - 1, memo, arr, target - arr[idx])
        else:
            take = 0

        no_take = self.recursion(idx - 1, memo, arr, target)

        memo[(idx, target)] =  take + no_take

        return memo[(idx, target)]
    
# --------------------------- Tabulation ---------------------------

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
    

# --------------------------- Space Optimization ---------------------------
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
        