# Tc:O(n), Sc: O(1)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # if there is a block in first cell -- then return 0
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            # there is one way to get there
            obstacleGrid[0][0] = 1
            
        # first row and column
        # if the current cell has no block ie obstacleGrid[i][0] == 0 and 
        # previous cell also had no block ie obstacleGrid[i-1][0] == 1 - so there was a way to get till there
        for row in range(1, m):
            if obstacleGrid[row][0] == 0 and obstacleGrid[row-1][0] == 1:
                obstacleGrid[row][0] = 1 # there is a way to get there 
            else:
                obstacleGrid[row][0] = 0 # there is no way to get there
        
        for col in range(1, n):
            if obstacleGrid[0][col] == 0 and obstacleGrid[0][col-1] == 1:
                obstacleGrid[0][col] = 1
            else:
                obstacleGrid[0][col] = 0
        
        # fill in the other cells
        for row in range(1, m):
            for col in range(1, n):
                # if there is no obstacle
                if obstacleGrid[row][col] == 0:
                    obstacleGrid[row][col] = obstacleGrid[row - 1][col] + obstacleGrid[row][col - 1]
                else:
                    obstacleGrid[row][col] = 0
        
        return obstacleGrid[-1][-1]