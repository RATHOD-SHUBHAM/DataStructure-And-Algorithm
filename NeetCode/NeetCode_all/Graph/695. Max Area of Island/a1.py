# With Visited Nodes ----------------------------------------------------------------------------------------

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False for _ in range(n)] for _ in range(m)]

        directions = [ (0, 1), (0,-1), (1,0), (-1,0) ]


        # Helper Function ------------------------------------------------------
        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0 or visited[row][col] == True:
                return 0

            visited[row][col] = True

            area = 0
            for adj_row, adj_col in directions:
                nei_row = adj_row + row
                nei_col = adj_col + col

                area += dfs(nei_row, nei_col)
            
            return 1 + area


        # Main Function ---------------------------------------------------------
        max_area = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or visited[i][j] == True:
                    continue
                
                area = dfs(i , j) # row , col

                max_area = max(max_area, area)
                
        
        return max_area
    

# Without Visited ----------------------------------------------------------------------------------------

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        directions = [ (0, 1), (0,-1), (1,0), (-1,0) ]


        # Helper Function ------------------------------------------------------
        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0:
                return 0

            grid[row][col] = 0 # Keep track of visited node

            area = 0
            for adj_row, adj_col in directions:
                nei_row = adj_row + row
                nei_col = adj_col + col

                area += dfs(nei_row, nei_col)
            
            return 1 + area


        # Main Function ---------------------------------------------------------
        max_area = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                
                area = dfs(i , j) # row , col

                max_area = max(max_area, area)
                
        
        return max_area