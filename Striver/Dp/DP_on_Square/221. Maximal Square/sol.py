"""
Solve this after solving: 1277. Count Square Submatrices with All Ones

Tc and Sc: O(m*n)

"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        # base case
        # col
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
        
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
        
        # logic
        for i in range(1, m):
            for j in range(1, n):
                if int(matrix[i][j]) == 0:
                    continue
                
                up = dp[i-1][j]
                left = dp[i][j-1]
                diagonal = dp[i-1][j-1]

                dp[i][j] = 1 + min(up, left, diagonal)
        
        max_square = 0
        for i in range(m):
            for j in range(n):
                max_square = max(max_square, dp[i][j])

        return pow(max_square, 2) # (max_square ** 2)