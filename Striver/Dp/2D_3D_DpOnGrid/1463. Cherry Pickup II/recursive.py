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

