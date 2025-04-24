# ---------- Recursion --------------
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        row = m-1
        col = n-1

        return self.recursive(row, col, m, n, obstacleGrid)
    
    def recursive(self, row, col, m, n, grid):
        if row < 0 or col < 0:
            return 0
        
        if row == 0 and col == 0:
            return 1
        
        if grid[row][col] == 1:
            return 0
        
        up = self.recursive(row-1, col, m, n, grid)
        left = self.recursive(row, col-1, m, n, grid)

        return up + left

        
# -------------- Memoization --------------
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        row = m-1
        col = n-1

        memo = {}

        return self.recursive(row, col, memo, m, n, obstacleGrid)
    
    def recursive(self, row, col, memo, m, n, grid):
        if row < 0 or col < 0:
            return 0
        
        if row == 0 and col == 0:
            return 1
        
        if grid[row][col] == 1:
            return 0
        
        if (row, col) in memo:
            return memo[(row, col)]
        
        up = self.recursive(row-1, col, memo, m, n, grid)
        left = self.recursive(row, col-1, memo, m, n, grid)

        memo[(row, col)] = up + left
        return memo[(row, col)]

        
# -------------- Tabulation --------------
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

# -------------- Space Optimization --------------
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


