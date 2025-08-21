class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        distinct_island = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                
                # Coordinate Normalization
                row_origin = i
                col_origin = j

                coords = []
                
                self.dfs(i, j, row_origin, col_origin, coords, grid, m, n)

                distinct_island.add(tuple(coords))
        
        return len(distinct_island)

    
    def dfs(self, i, j, row_origin, col_origin, coords, grid, m, n):
        # base case
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
            return

        # Coordinate Normalization
        row_no = i - row_origin
        col_no = j - col_origin

        coords.append((row_no, col_no))

        grid[i][j] = 0

        # Explore Neighbors
        neighbors = [[0,-1], [0,1], [-1,0], [1,0]]
        for nei in neighbors:
            nei_row = nei[0] + i
            nei_col = nei[1] + j

            self.dfs(nei_row, nei_col, row_origin, col_origin, coords, grid, m, n)
        
        return coords