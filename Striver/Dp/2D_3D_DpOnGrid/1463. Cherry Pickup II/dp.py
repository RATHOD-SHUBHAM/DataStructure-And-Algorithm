class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # Initialize with negative infinity for invalid states
        dp = [[[-math.inf for _ in range(n)] for _ in range(n)] for _ in range(m)]

        # Fill first row - robots start at opposite ends
        # The first row should only have a valid value at the starting positions (0,0) and (0,n-1).
        dp[0][0][n-1] = grid[0][0] + grid[0][n-1]  # Start positions
        
        for row in range(1, m):
            for c1 in range(n):
                for c2 in reversed(range(n)):
                    # Try all possible moves from previous row
                    for prev_c1 in [c1-1, c1, c1+1]:
                        for prev_c2 in [c2-1, c2, c2+1]:
                            # Check if previous positions are within bounds
                            if 0 <= prev_c1 < n and 0 <= prev_c2 < n:
                                # Update if we can reach current state with better result
                                dp[row][c1][c2] = max(dp[row][c1][c2], dp[row-1][prev_c1][prev_c2])
                    
                    # If this state can be reached from a valid previous state
                    # This check is crucial because it ensures we only add cherries to positions that can actually be reached through valid paths.
                    if dp[row][c1][c2] != -math.inf:
                        # Add cherries from current row
                        if c1 == c2:
                            dp[row][c1][c2] += grid[row][c1]  # Count only once if same cell
                        else:
                            dp[row][c1][c2] += grid[row][c1] + grid[row][c2]

        # Find maximum cherries in the last row
        result = -math.inf
        for c1 in range(n):
            for c2 in range(n):
                result = max(result, dp[m-1][c1][c2])
        
        return max(0, result)  # Return 0 if no valid path