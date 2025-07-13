class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[[[-math.inf for _ in range(n)]for _ in range(m)]for _ in range(n)]for _ in range(m)]

        # Base case: both start at (0,0)
        if grid[0][0] != -1:
            dp[0][0][0][0] = grid[0][0]

        for r1 in range(m):
            for c1 in range(n):
                for r2 in range(m):
                    for c2 in range(n):
                        # Check if there is thorn
                        if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                            continue

                        cherries = grid[r1][c1]

                        if r1 != r2 or c1 != c2:
                            cherries += grid[r2][c2]

                        best_prev = -math.inf
                    
                        # Both moved down
                        if r1 > 0 and r2 > 0:
                            best_prev = max(best_prev, dp[r1-1][c1][r2-1][c2])
                        
                        # Both moved right
                        if c1 > 0 and c2 > 0:
                            best_prev = max(best_prev, dp[r1][c1-1][r2][c2 - 1])
                        
                        # Person 1 down, Person 2 right
                        if r1 > 0 and c2 > 0:
                            best_prev = max(best_prev, dp[r1-1][c1][r2][c2-1])
                        
                        # Person 1 right, Person 2 down
                        if c1 > 0 and r2 > 0:
                            best_prev = max(best_prev, dp[r1][c1-1][r2-1][c2])
                        
                        # If we can reach this state from a previous state
                        if best_prev != -math.inf:
                            dp[r1][c1][r2][c2] = best_prev + cherries
            
        # Check if there's a valid path to the bottom-right corner
        if dp[m-1][n-1][m-1][n-1] == -math.inf:
            return 0
        else:
            return dp[m-1][n-1][m-1][n-1]


# ----------------------------------- Cutting Down c2 -----------------------------------

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