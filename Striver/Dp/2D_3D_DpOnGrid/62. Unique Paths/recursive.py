class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.recursion(m-1, n-1)
    
    def recursion(self, row, col):
        if row < 0 or col < 0:
            return 0
        
        if row == 0 and col == 0:
            return 1
        
        # move up
        up = self.recursion(row-1, col)

        # move left
        down = self.recursion(row, col-1)

        return up + down