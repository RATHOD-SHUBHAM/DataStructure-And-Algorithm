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

        
