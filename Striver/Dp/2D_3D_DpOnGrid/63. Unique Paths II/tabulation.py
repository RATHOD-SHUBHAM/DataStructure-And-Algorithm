class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        dp = [[1 for j in range(n)]for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                
                up = dp[i-1][j] if i-1 >= 0 else 0
                left = dp[i][j-1] if j-1 >= 0 else 0

                dp[i][j] = up + left
            
        return dp[-1][-1]