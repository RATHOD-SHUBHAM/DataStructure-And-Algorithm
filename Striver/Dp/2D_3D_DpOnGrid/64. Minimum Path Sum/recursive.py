class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        row = m-1
        col = n-1

        return self.recursive(row, col, m, n, grid)
    
    def recursive(self, row, col, m, n, grid):
        if row < 0 or col < 0:
            return math.inf
        
        if row == 0 and col == 0:
            return grid[0][0]
        
        up = self.recursive(row-1, col, m, n, grid)
        left = self.recursive(row, col-1, m, n, grid)

        path_cost = grid[row][col] + min(up , left)

        return path_cost