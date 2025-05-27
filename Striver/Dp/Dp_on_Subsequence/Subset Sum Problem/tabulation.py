class Solution:
    def isSubsetSum (self, arr, sum):
        # code here
        n = len(arr)
        
        """
        Why we created a 2D DP array:
        In the original recursive approach, we were tracking two changing parameters:
        
        idx: The current index in the array we're considering (0 to n-1)
        target: The remaining sum we need to achieve
        
        
        Since we have two changing parameters, we need a 2D array to represent all possible states:
        
        Each cell dp[i][j] represents: "Can we form sum j using elements from index 0 to i-1?"
        """
        
        # Change dimension to n+1 to handle base case properly
        
        dp = [[False for _ in range(sum+1)]for _ in range(n)]
        
        # Base case: empty subset can form sum = 0
        """
        When target sum is 0, we can always achieve it by selecting no elements (empty subset)
        This translates to: dp[i][0] = True for all i (any number of elements can form a sum of 0)
        """
        for i in range(n):
            dp[i][0] = True
        
        if sum >= arr[0]:
            dp[0][arr[0]] = True
        
        # number of ways to achieve sum j using first i numbers
        for idx in range(1, n):
            for target in range(1, sum+1):
                if target >= arr[idx]:
                    take = dp[idx-1][target - arr[idx]]
                else:
                    take = False
                
                dont_take = dp[idx-1][target]
                
                dp[idx][target] = take or dont_take
        
        return dp[n-1][sum]