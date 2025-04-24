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
    
# ---------------- Memoization ----------------
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

# ---------------- Tabulation ----------------
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[math.inf for _ in range(n)]for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                left = dp[i][j-1] if j-1 >= 0 else math.inf
                up = dp[i-1][j] if i-1 >= 0 else math.inf

                dp[i][j] = grid[i][j] + min(left, up)
        
        return dp[-1][-1]

# ---------------- Space Optimization ----------------
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [0] * n
        dp[0] = grid[0][0]

        # First Row
        for j in range(1, n):
            dp[j] = grid[0][j] + dp[j-1]

        # Remaining Row
        for i in range(1, m):
            # Fill in the first column
            dp[0] = grid[i][0] + dp[0]
            
            for j in range(1, n):
                left = dp[j-1]
                up = dp[j]

                dp[j] = grid[i][j] + min(left, up)
        
        return dp[-1]

