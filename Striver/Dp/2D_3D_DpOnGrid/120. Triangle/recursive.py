class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        n = len(triangle[0])

        row = 0
        col = 0

        return self.recursion(row, col, m, n, triangle)
    
    def recursion(self, row, col, m, n, triangle):
        # base case
        if row >= m:
            return 0
        
        down = self.recursion(row+1, col, m, n, triangle)
        down_right = self.recursion(row+1, col+1, m, n, triangle)

        cur_path_sum = triangle[row][col] + min(down, down_right)

        return cur_path_sum