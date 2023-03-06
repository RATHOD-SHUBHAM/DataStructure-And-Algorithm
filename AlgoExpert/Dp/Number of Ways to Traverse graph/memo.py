# Tc: O(m + n) | Sc: O(m + n) + O(n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # start row and col
        i = 0
        j = 0
        
        memo = [[None for _ in range(n)] for _ in range(m)]
        
        return self.getPath(i , j , m , n, memo)
        
    def getPath(self, i , j , m , n, memo):
        # base case
        if i == m or j == n:
            return 0
        
        if i == m - 1 and j == n - 1:
            return 1
        
        if memo[i][j] is not None:
            return memo[i][j]
        
        right = self.getPath(i , j + 1, m , n, memo)
        down = self.getPath(i + 1 , j, m , n, memo)
        
        memo[i][j] = right + down
        
        return memo[i][j]