class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        n = len(triangle[-1])

        min_path_sum = math.inf
        i = m - 1
        for j in reversed(range(n)):
            cur_path_sum = self.recursion(i, j, triangle)
            min_path_sum = min(min_path_sum, cur_path_sum)
        
        return min_path_sum
    
    def recursion(self, i, j, grid):
        # base case
        if i == 0 and j == 0:
            return grid[0][0]
        
        if i < 0 or j < 0 or j >= len(grid[i]):
            return math.inf
        
        # Logic
        up = self.recursion(i - 1, j, grid)
        left = self.recursion(i - 1, j - 1, grid)

        return grid[i][j] + min(up, left)