# Tc and Sc: O(n)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        dp[1][1] = 1 if obstacleGrid[0][0] != 1 else 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                if i == 1 and j == 1:
                    continue
                    
                if obstacleGrid[i-1][j-1] != 1:
                    left = dp[i][j - 1]
                    up = dp[i-1][j]
                    dp[i][j] = up + left
        
        return dp[-1][-1]
        
        