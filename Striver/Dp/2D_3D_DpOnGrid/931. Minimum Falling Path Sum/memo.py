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