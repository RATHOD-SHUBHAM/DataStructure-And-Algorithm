class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for j in range(n)] for i in range(m)]
        
        # There is only one way to reach from start to start
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                    
                up = dp[i-1][j] if i-1 >= 0 else 0
                left = dp[i][j-1] if j-1 >= 0 else 0

                dp[i][j] = up + left
        
        return dp[-1][-1]