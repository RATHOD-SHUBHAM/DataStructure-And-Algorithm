"""
Traverse from top to bottom
Then once you reach the bottom
Traverse from bottom to top
"""

class Solution:
    def __init__(self):
        self.max_cherry_picked = 0

    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        row = 0
        col = 0
        cur_cherry_picked = 0
        self.top_to_bottom(row, col, m, n, cur_cherry_picked, grid)

        return self.max_cherry_picked
    
    def top_to_bottom(self, row, col, m, n, cur_cherry_picked, grid):
        # Base case
        if row >= m or col >= n or grid[row][col] == -1:
            return 0
        
        # If we have reached the bottom, then we need to traverse back to top
        if row == m-1 and col == n-1:
            self.bottom_to_top(row, col, m, n, cur_cherry_picked, grid)
            return
        
        # Other cells
        cherry = grid[row][col] # This can be 0 or 1
        grid[row][col] = 0 # Mark as picked
        
        # Move down
        self.top_to_bottom(row+1, col, m, n, cur_cherry_picked + cherry, grid)

        # Move right
        self.top_to_bottom(row, col+1, m, n, cur_cherry_picked + cherry, grid)

        grid[row][col] = cherry # Put back the cherry for other paths to explore

        return 

    def bottom_to_top(self, row, col, m, n, cur_cherry_picked, grid):
        # Base case
        if row < 0 or col < 0 or grid[row][col] == -1:
            return 0
        
        # If we reached the start cell
        if row == 0 and col == 0:
            self.max_cherry_picked = max(self.max_cherry_picked, (cur_cherry_picked+grid[0][0]) )
            return 
        
        # Other cells
        cherry = grid[row][col] # This can be 0 or 1
        grid[row][col] = 0 # Mark as picked
        
        # Move up
        self.bottom_to_top(row-1, col, m, n, cur_cherry_picked + cherry, grid)

        # Move left
        self.bottom_to_top(row, col-1, m, n, cur_cherry_picked + cherry, grid)

        grid[row][col] = cherry # Put back the cherry for other paths to explore

        return 