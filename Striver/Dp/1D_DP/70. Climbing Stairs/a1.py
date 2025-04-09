# -------------------------- Brute Force: Recursion --------------------------
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        
        if n == 0:
            return 1
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    
# -------------------------- Memoization --------------------------
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
    
# -------------------------- Tabulation --------------------------
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
            
        dp = [-1] * (n + 1)
        
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

# -------------------------- Space Optimization --------------------------
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        p_prev = 1
        prev = 2
        
        for i in range(3, n+1):
            cur_ways = prev + p_prev
            p_prev = prev
            prev = cur_ways
        
        return cur_ways