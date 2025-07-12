class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[math.inf for _ in range(n)]for _ in range(m)]

        # basecase
        for j in range(n):
            dp[0][j] = matrix[0][j]
        
        for i in range(1, m):
            for j in range(n):
                # Logic
                up = dp[i-1][j]
                left = dp[i-1][j-1] if j-1 >= 0 else math.inf
                right = dp[i-1][j+1] if j+1 < n else math.inf

                dp[i][j] = matrix[i][j] + min(up, left, right)
        
        return min(dp[m-1])