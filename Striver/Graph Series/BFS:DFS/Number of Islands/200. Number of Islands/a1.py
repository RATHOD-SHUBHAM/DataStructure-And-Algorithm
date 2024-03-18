# Tc: O(n^2) | Sc: O(n)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        visited = [[False for _ in range(n)]for _ in range(m)]
        
        # helper code ----------
        
        def explore_border_dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == "0" or visited[i][j] == True:
                return
            
            visited[i][j] = True
            
            # explore 4 directions
            explore_border_dfs(i + 1, j)
            explore_border_dfs(i - 1, j)
            explore_border_dfs(i, j + 1)
            explore_border_dfs(i, j - 1)
            
            return

        
        # main code --------------------------
        
        no_of_island = 0
        
        for i in range(m):
            for j in range(n):
                
                if visited[i][j] == True:
                    continue
                
                if grid[i][j] == "1":
                    no_of_island += 1

                    explore_border_dfs(i , j)
                
        return no_of_island
    
# -------------------------------------------Solution 2-----------------------------------------------------

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        no_of_island = 0

        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        visited = [[False for _ in range(n)] for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "0" or visited[row][col] == True:
                    continue

                self.dfs(row, col, visited, neighbors, m , n, grid)

                no_of_island += 1

        return no_of_island
    
    def dfs(self, row, col, visited, neighbors, m , n, grid):
        if row < 0 or col < 0 or row >= m or col >= n or visited[row][col] == True or grid[row][col] == "0":
            return
        
        visited[row][col] = True

        for neighbor in neighbors:
            adj_row, adj_col = neighbor

            nei_row = row + adj_row
            nei_col = col + adj_col

            self.dfs(nei_row, nei_col, visited, neighbors, m , n, grid)
        
        return
