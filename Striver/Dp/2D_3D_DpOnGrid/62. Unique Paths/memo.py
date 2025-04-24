class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = m-1
        col = n-1

        memo = {}
        return self.recursion(row, col, memo)
    
    def recursion(self, row, col, memo):
        if row < 0 or col < 0:
            return 0
        
        if row == 0 and col == 0:
            return 1
        
        if (row, col) in memo:
            return memo[(row, col)]
        
        # move up
        up = self.recursion(row-1, col, memo)

        # move left
        down = self.recursion(row, col-1, memo)

        memo[(row, col)] = up + down
        
        return memo[(row, col)]