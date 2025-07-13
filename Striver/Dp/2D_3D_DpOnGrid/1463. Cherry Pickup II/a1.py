import math
from typing import List

# --------------------------- Recursion ---------------------
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        r1 = 0
        c1 = 0
        r2 = 0
        c2 = n-1

        return self.recursion(r1,c1,r2,c2,m,n,grid)
    
    def recursion(self, r1,c1,r2,c2,m,n,grid):
        # base case
        if c1 < 0 or c1 >= n or c2 < 0 or c2 >= n:
            return -math.inf
        
        if r1 == m-1 and r2 == m-1:
            result = grid[r1][c1]

            if c1 != c2:
                result += grid[r2][c2]
            
            return result
        
        result = grid[r1][c1]

        if c1 != c2:
            result += grid[r2][c2]
        
        # 1: Move Down_Left
        # 1: down_left, 2: down_left
        DL_DL = self.recursion(r1 + 1 , c1 - 1, r2 + 1, c2 - 1, m,n,grid)

        # 1: down_left, 2: down
        DL_D = self.recursion(r1 + 1 , c1 - 1, r2 + 1, c2, m,n,grid)

        # 1: down_left, 2: down_right
        DL_DR = self.recursion(r1 + 1 , c1 - 1, r2 + 1, c2 + 1, m,n,grid)

        # 1: Move Down
        # 1: down, 2: down_left
        D_DL = self.recursion(r1 + 1 , c1, r2 + 1, c2 - 1, m,n,grid)

        # 1: down, 2: down
        D_D = self.recursion(r1 + 1 , c1, r2 + 1, c2, m,n,grid)

        # 1: down, 2: down_right
        D_DR = self.recursion(r1 + 1 , c1, r2 + 1, c2 + 1, m,n,grid)

        # 1: Move Down Right
        # 1: down_right, 2: down_left
        DR_DL = self.recursion(r1 + 1 , c1 + 1, r2 + 1, c2 - 1, m,n,grid)

        # 1: down_right, 2: down
        DR_D = self.recursion(r1 + 1 , c1 + 1, r2 + 1, c2, m,n,grid)

        # 1: down_right, 2: down_right
        DR_DR = self.recursion(r1 + 1 , c1 + 1 , r2 + 1, c2 + 1, m,n,grid)

        
        result += max(
            DL_DL, DL_D, DL_DR,
            D_DL, D_D, D_DR,
            DR_DL, DR_D, DR_DR
        )

        return result
    
# --------------------------- same solution ---------------------
"""
Instead of making each call manually, we can use a loop to iterate over the possible moves.
"""

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        r1 = 0
        c1 = 0
        r2 = 0
        c2 = n-1

        return self.recursion(r1,c1,r2,c2,m,n,grid)
    
    def recursion(self, r1,c1,r2,c2,m,n,grid):
        # base case
        if c1 < 0 or c1 >= n or c2 < 0 or c2 >= n:
            return -math.inf
        
        if r1 == m-1 and r2 == m-1:
            result = grid[r1][c1]

            if c1 != c2:
                result += grid[r2][c2]
            
            return result
        
        result = grid[r1][c1]

        if c1 != c2:
            result += grid[r2][c2]

        max_cherry = -math.inf
        for col1 in (c1-1, c1, c1+1):
            for col2 in (c2-1, c2, c2+1):
                cherry_picked = self.recursion(r1 + 1 , col1, r2 + 1, col2, m,n,grid)
                max_cherry = max(max_cherry, cherry_picked)
        
        result += max_cherry

        return result
    
# --------------------------- same solution ---------------------
"""
From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1)

This means both the robots move to the next row at the same time

so instead of calling r1 r2 , we can simply call row
"""
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        row = 0
        c1 = 0
        c2 = n-1

        return self.recursion(row, c1, c2, m, n, grid)
    
    def recursion(self, row, c1, c2, m, n, grid):
        # base case
        if c1 < 0 or c1 >= n or c2 < 0 or c2 >= n:
            return -math.inf
        
        if row == m-1:
            result = grid[row][c1]

            if c1 != c2:
                result += grid[row][c2]
            
            return result
        
        result = grid[row][c1]

        if c1 != c2:
            result += grid[row][c2]

        max_cherry = -math.inf
        for col1 in (c1-1, c1, c1+1):
            for col2 in (c2-1, c2, c2+1):
                cherry_picked = self.recursion(row + 1 , col1, col2, m,n,grid)
                max_cherry = max(max_cherry, cherry_picked)
        
        result += max_cherry

        return result


# --------------------------- Memoization ---------------------
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        row = 0
        c1 = 0
        c2 = n-1

        memo = {}

        return self.recursion(row, c1, c2, memo, m, n, grid)
    
    def recursion(self, row, c1, c2, memo, m, n, grid):
        # base case
        if c1 < 0 or c1 >= n or c2 < 0 or c2 >= n:
            return -math.inf
        
        if row == m-1:
            result = grid[row][c1]

            if c1 != c2:
                result += grid[row][c2]
            
            return result
        
        if (row, c1, c2) in memo:
            return memo[(row, c1, c2)]
        
        result = grid[row][c1]

        if c1 != c2:
            result += grid[row][c2]

        max_cherry = -math.inf
        for col1 in (c1-1, c1, c1+1):
            for col2 in (c2-1, c2, c2+1):
                cherry_picked = self.recursion(row + 1 , col1, col2, memo, m,n,grid)
                max_cherry = max(max_cherry, cherry_picked)
        
        result += max_cherry

        memo[(row, c1, c2)] = result

        return memo[(row, c1, c2)]

# --------------------------- Tabulation ---------------------
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