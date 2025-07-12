class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        min_sum = math.inf
        i = m - 1
        for j in reversed(range(n)):
            cur_sum = self.recursion(i, j, {}, matrix)
            min_sum = min(cur_sum, min_sum)
        
        return min_sum
    
    def recursion(self, i, j, memo, matrix):
        # base case
        if i == 0 and (j >= 0 and j < len(matrix)):
            return matrix[0][j]
        
        if i < 0 or j < 0 or j >= len(matrix):
            return math.inf
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        # Logic
        up = self.recursion(i-1, j, memo, matrix)
        left = self.recursion(i-1, j-1, memo, matrix)
        right = self.recursion(i-1, j+1, memo, matrix)

        memo[(i,j)] = matrix[i][j] + min(up, left, right)
        return memo[(i, j)]