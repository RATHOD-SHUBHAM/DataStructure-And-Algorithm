class Solution:
    def fib(self, n: int) -> int:
        dp = [0,1]
        
        for i in range(2, n+1):
            new_fib = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = new_fib
        
        return dp[1] if n > 0 else dp[0]
        