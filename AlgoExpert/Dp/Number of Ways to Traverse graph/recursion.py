# time = O(2 ^ (m + n))
# Space = O(m + n)

# brute force
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # start row and col
        i = 0
        j = 0
        
        return self.getPath(i , j , m , n)
        
    def getPath(self, i , j , m , n):
        # base case
        if i == m or j == n:
            return 0
        
        if i == m - 1 and j == n - 1:
            return 1
        
        right = self.getPath(i , j + 1, m , n)
        down = self.getPath(i + 1 , j, m , n)
        
        return right + down
        