class Solution:
    def __init__(self):
        self.mod = (10 ** 9) + 7
        
    def fib_memo(self, n, dp):
        if dp[n] != -1:
            return dp[n]
        elif n <= 1:
            dp[n] = n
            return dp[n]
        else:
            dp[n] = self.fib_memo(n - 1, dp) + self.fib_memo(n - 2, dp)
            
            return dp[n]
            
    def topDown(self, n):
        # Memoization
        dp = [-1] * (n + 1)
        val = self.fib_memo(n, dp)

        return val % self.mod
    
    def bottomUp(self, n):
        if n <= 1:
            return n
        # Tabulation
        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n] % self.mod