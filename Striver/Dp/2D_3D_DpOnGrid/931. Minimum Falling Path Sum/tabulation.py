class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0 for _ in range(n)]for _ in range(m)]
        # Fill in first row
        for i in range(n):
            dp[0][i] = matrix[0][i]
        
        for i in range(1, m):
            for j in range(n):
                # up
                up =dp[i-1][j]

                # diagonals
                diag_left = dp[i-1][j-1] if j-1 >= 0 else math.inf
                diag_right = dp[i-1][j+1] if j+1 < n else math.inf

                dp[i][j] = matrix[i][j] + min(up, diag_left, diag_right)
        
        return min(dp[-1])