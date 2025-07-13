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
            return
        
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
            return
        
        # If we reached the start cell
        if row == 0 and col == 0:
            cur_cherry_picked += grid[0][0] # Add the cherry at the start cell
            self.max_cherry_picked = max(self.max_cherry_picked, cur_cherry_picked )
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
    
# ---------------------------- MEMOIZATION ---------------------------- #
# Check memo.py for clear explanation of the memoization approach
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        memo = {}

        r1 = 0
        c1 = 0
        r2 = 0

        total_cherry_picked = self.memoization(r1, c1, r2, n, memo, grid)

        return max(0, total_cherry_picked)

    def memoization(self, r1, c1, r2, n, memo, grid):
        # compute c2
        c2 = r1 + c1 - r2

        # base case
        if r1 >= n or c1 >= n or r2 >= n or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
            return -math.inf
        
        # End cell
        if r1 == n - 1 and c1 == n - 1:
            return grid[n-1][n-1]
        
        if (r1, c1, r2) in memo:
            return memo[(r1, c1, r2)]
        
        result = grid[r1][c1]
        # check if both person are not on same cell
        if r1 != r2 or c1 != c2:
            result += grid[r2][c2]
        

        result += max(
            self.memoization(r1+1, c1, r2, n, memo, grid),
            self.memoization(r1, c1+1, r2, n, memo, grid),
            self.memoization(r1+1, c1, r2+1, n, memo, grid),
            self.memoization(r1, c1+1, r2+1, n, memo, grid)
        )

        memo[(r1, c1, r2)] = result
        return memo[(r1, c1, r2)]
    

# ---------------------------- TABULATION ---------------------------- #
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Create a 4D DP table
        # dp[r1][c1][r2][c2] represents max cherries with person 1 at (r1,c1) and person 2 at (r2,c2)
        # We can optimize to dp[r1][c1][r2] since c2 = r1 + c1 - r2
        
        # Initialize with -inf (representing invalid paths)
        dp = [[[-math.inf for _ in range(n)] for _ in range(n)] for _ in range(n)]
        # Each cell represents the maximum cherries that can be collected with Person 1 at position (r1, c1) and Person 2 at position (r2, c2).
        
        # Fill the table bottom-up
        for r1 in range(n):
            for c1 in range(n):
                for r2 in range(n):
                    # Calculate c2 based on r1, c1, r2
                    c2 = r1 + c1 - r2
                    
                    # Skip invalid states
                    if c2 < 0 or c2 >= n:
                        continue
                    
                    # Skip if either position has a thorn
                    if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                        continue
                    
                    # Base case: both at the starting position
                    if r1 == 0 and c1 == 0 and r2 == 0:
                        dp[r1][c1][r2] = grid[0][0]  # Only count once
                        continue
                    
                    # Calculate cherries for current state
                    cherries = 0
                    if r1 == r2 and c1 == c2:
                        # Same cell, count cherry only once
                        cherries = grid[r1][c1]
                    else:
                        # Different cells, count both cherries
                        cherries = grid[r1][c1] + grid[r2][c2]
                    
                    # Check all possible previous states that could lead to this state
                    # Update current state with best previous state + current cherries
                    
                    # There are 4 possible previous states:
                    # 1. Both moved down: (r1-1, c1, r2-1, c2)
                    # 2. Both moved right: (r1, c1-1, r2, c2-1)
                    # 3. Person 1 down, Person 2 right: (r1-1, c1, r2, c2-1)
                    # 4. Person 1 right, Person 2 down: (r1, c1-1, r2-1, c2)
                    
                    best_prev = -math.inf
                    
                    # Both moved down
                    if r1 > 0 and r2 > 0:
                        best_prev = max(best_prev, dp[r1-1][c1][r2-1])
                    
                    # Both moved right
                    if c1 > 0 and c2 > 0:
                        best_prev = max(best_prev, dp[r1][c1-1][r2])
                    
                    # Person 1 down, Person 2 right
                    if r1 > 0 and c2 > 0:
                        best_prev = max(best_prev, dp[r1-1][c1][r2])
                    
                    # Person 1 right, Person 2 down
                    if c1 > 0 and r2 > 0:
                        best_prev = max(best_prev, dp[r1][c1-1][r2-1])
                    
                    # If we can reach this state from a previous state
                    if best_prev != -math.inf:
                        dp[r1][c1][r2] = best_prev + cherries
        
        # Check if there's a valid path to the bottom-right corner
        if dp[n-1][n-1][n-1] == -math.inf:
            return 0
        else:
            return dp[n-1][n-1][n-1]