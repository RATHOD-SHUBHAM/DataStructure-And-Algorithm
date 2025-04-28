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