# Tc and Sc: O(m * n)
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        # Step 1: Explore boundaries for Land Cell
        for col in range(n):
            # First row
            self.dfs(0, col, directions, grid, m, n)
            
            # Last row
            self.dfs(m-1, col, directions, grid, m, n)

        for row in range(m):
            # First Column
            self.dfs(row, 0, directions, grid, m, n)
            
            # Last Column
            self.dfs(row, n-1, directions, grid, m, n)

        
        #Step 2: Count the land cell
        # land = 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             land += 1

        land = 0
        for i in range(m):
            land += sum(grid[i])
        
        return land
    
    def dfs(self, i, j, directions, grid, m, n):
        # base case
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
            return
        
        # Flip 1 -> -1
        grid[i][j] = 0

        for nei in directions:
            nei_i = i + nei[0]
            nei_j = j + nei[1]

            self.dfs(nei_i, nei_j, directions, grid, m, n)
        
        return