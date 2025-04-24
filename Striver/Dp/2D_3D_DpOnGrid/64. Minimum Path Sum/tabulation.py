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