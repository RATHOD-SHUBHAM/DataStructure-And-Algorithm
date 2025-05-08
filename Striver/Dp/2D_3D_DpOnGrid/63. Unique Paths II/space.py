class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        dp = [0] * n
        dp[0] = 1
        
        # Fill dp as per the first row
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                dp[j] = 0
            else:
                dp[j] = dp[j-1] # as per the previous cell
        
        # For the remaining row
        for i in range(1, m):
            # Check if there is a obstacle in first col
            if obstacleGrid[i][0] == 1:
                dp[0] = 0
            
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    dp[j] = dp[j] + dp[j-1]
        
        return dp[-1]

# ----------------------------- Same Solution ------------------------------
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] == 1:
            return 0

        dp = [0 for _ in range(n)]
        dp[0] = 1
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                if grid[i][j] == 1:
                    dp[j] = 0
                    continue
                
                up = dp[j] if i - 1 >= 0 else 0
                left = dp[j-1] if j-1 >= 0 else 0
                
                dp[j] = up + left
        

        return dp[-1]