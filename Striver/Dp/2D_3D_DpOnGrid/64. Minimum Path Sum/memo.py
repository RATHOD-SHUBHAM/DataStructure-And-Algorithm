class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        row = m-1
        col = n-1

        memo = {}

        return self.recursive(row, col, memo, m, n, grid)
    
    def recursive(self, row, col, memo, m, n, grid):
        if row < 0 or col < 0:
            return math.inf
        
        if row == 0 and col == 0:
            return grid[0][0]
        
        if (row, col) in memo:
            return memo[(row, col)]
        
        up = self.recursive(row-1, col, memo, m, n, grid)
        left = self.recursive(row, col-1, memo, m, n, grid)

        path_cost = grid[row][col] + min(up , left)

        memo[(row, col)] = path_cost

        return memo[(row, col)]
        

