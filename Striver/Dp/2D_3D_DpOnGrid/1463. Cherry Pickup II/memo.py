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