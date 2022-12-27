class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: 
            return 0
        if n == 1 or n == 2:
            return 1
        
        dp = [0, 1, 1]
        
        for i in range(3, n + 1):
            new_value = dp[0] + dp[1] + dp[2]
            dp[0] = dp[1]
            dp[1] = dp[2]
            dp[2] = new_value
            
        
        return dp[-1]