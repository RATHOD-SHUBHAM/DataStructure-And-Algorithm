# ---------------------- Recursion ----------------------

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        min_path = math.inf
        row = 0
        for col in range(n):
            cur_path = self.recursion(row, col, m, n, matrix)
            min_path = min(min_path, cur_path)
        
        return min_path
    
    def recursion(self, row, col, m, n, matrix):
        # base case
        if row >= m:
            return 0
        
        if col < 0 or col >= n:
            return math.inf
        
        # down
        down = self.recursion(row+1, col, m, n, matrix)

        # diagonals
        diag_left = self.recursion(row+1, col-1, m, n, matrix)
        diag_right = self.recursion(row+1, col+1, m, n, matrix)

        cur_path = matrix[row][col] + min(down, diag_left, diag_right)

        return cur_path

# ---------------------- Memoization ----------------------
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        min_path = math.inf
        row = 0
        for col in range(n):
            memo = {}
            cur_path = self.recursion(row, col, memo, m, n, matrix)
            min_path = min(min_path, cur_path)
        
        return min_path
    
    def recursion(self, row, col, memo, m, n, matrix):
        # base case
        if row >= m:
            return 0
        
        if col < 0 or col >= n:
            return math.inf
        
        if (row, col) in memo:
            return memo[(row, col)]
        
        # down
        down = self.recursion(row+1, col, memo, m, n, matrix)

        # diagonals
        diag_left = self.recursion(row+1, col-1, memo, m, n, matrix)
        diag_right = self.recursion(row+1, col+1, memo, m, n, matrix)

        cur_path = matrix[row][col] + min(down, diag_left, diag_right)

        memo[(row, col)] = cur_path

        return memo[(row, col)]

# ---------------------- Tabulation ----------------------
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

# ---------------------- Space Optimization ----------------------
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