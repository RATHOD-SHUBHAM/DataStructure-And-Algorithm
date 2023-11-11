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