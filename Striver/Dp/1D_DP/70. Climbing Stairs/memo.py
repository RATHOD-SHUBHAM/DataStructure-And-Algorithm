class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        return self.memo(dp, n)
    
    def memo(self, dp, n):
        if n < 0:
            return 0
        
        if n == 0:
            return 1

        if dp[n] != -1:
            return dp[n]
        
        dp[n] = self.memo(dp, n-1) + self.memo(dp, n-2)

        return dp[n]