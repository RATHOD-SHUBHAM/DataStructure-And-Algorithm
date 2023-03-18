class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # recursive solution
        i = 0
        j = 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        return self.traversePath(i , j , m, n , obstacleGrid)
    
    def traversePath(self, i , j , m, n, obstacleGrid):
        # base case
        if i == m - 1 and j == n - 1:
            return 1
        
        if i == m or j == n:
            return 0
        
        if obstacleGrid[i][j] == 1:
            return 0
        
        right = self.traversePath(i , j + 1 , m, n ,obstacleGrid)
        down = self.traversePath(i + 1 , j , m, n ,obstacleGrid)
        
        return right + down