class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        n = len(triangle[0])

        row = 0
        col = 0

        memo = {}

        return self.recursion(row, col, memo, m, n, triangle)
    
    def recursion(self, row, col, memo, m, n, triangle):
        # base case
        if row >= m:
            return 0
        
        if (row, col) in memo:
            return memo[(row,col)]
        
        down = self.recursion(row+1, col, memo, m, n, triangle)
        down_right = self.recursion(row+1, col+1, memo, m, n, triangle)

        cur_path_sum = triangle[row][col] + min(down, down_right)

        memo[(row,col)] = cur_path_sum

        return memo[(row,col)]