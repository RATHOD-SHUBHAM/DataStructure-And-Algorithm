class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [0 for _ in range(n)]
        # Fill in first row
        for i in range(n):
            dp[i] = matrix[0][i]
        
        for i in range(1, m):
            temp = [0 for _ in range(n)]
            for j in range(n):
                # up
                up = dp[j]

                # diagonals
                diag_left = dp[j-1] if j-1 >= 0 else math.inf
                diag_right = dp[j+1] if j+1 < n else math.inf

                temp[j] = matrix[i][j] + min(up, diag_left, diag_right)
            
            dp = temp
        
        return min(dp)