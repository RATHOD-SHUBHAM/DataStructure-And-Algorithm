# No of island - DFS 
# This will only return the number of island

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        
        # Add land -------------
        for land in positions:
            row , col = land
            grid[row][col] = 1
        
        print(grid)
        
        # DFS to get the no of Island ----------
        def dfs(i,j):
            if i < 0 or j < 0 or i >= m or j >= n or visited[i][j] == True or grid[i][j] == 0:
                return
            
            visited[i][j] = True
            
            up = dfs(i - 1, j)
            down = dfs(i + 1 , j)
            left = dfs(i, j - 1)
            right = dfs(i , j + 1)
            
            return
            
            
        # Main Code ----------------------
        no_of_island = 0
        
        for i in range(m):
            for j in range(n):
                if visited[i][j] == False and grid[i][j] == 1:
                    dfs(i , j)
                    no_of_island += 1
            
        print(no_of_island)