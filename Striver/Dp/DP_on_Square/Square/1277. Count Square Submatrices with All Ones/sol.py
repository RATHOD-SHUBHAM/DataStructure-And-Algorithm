"""
For a 2x2 square ending at (i, j), the following conditions must be met:

    * The cell at (i, j) must be 1.
    * The cells above (i-1, j), to the left (i, j-1), and diagonally (i-1, j-1) must also be 1.

Tc: O(m * n)
Sc: O(m * n)
"""
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        # the maximum size of square (ending at (i, j))
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # base case
        for i in range(m):
            if matrix[i][0] == 0:
                continue
            
            dp[i][0] = 1
        
        for j in range(n):
            if matrix[0][j] == 0:
                continue
            
            dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    continue
                
                # To form a square of size k ending at (i, j), you need a square of size k-1 ending at all 3 of those neighbors.
                left = dp[i][j-1]
                up = dp[i-1][j]
                diagonal = dp[i-1][j-1]

                # min() ensures **we always build a square, not a rectangle.
                dp[i][j] = 1 + min(left, up, diagonal) # The min() ensures all sides must be part of a valid square
        
        total_square = 0
        for i in range(m):
            for j in range(n):
                total_square += dp[i][j]
        
        return total_square  