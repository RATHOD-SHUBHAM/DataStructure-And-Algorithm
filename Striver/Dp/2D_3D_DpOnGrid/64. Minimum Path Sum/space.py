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