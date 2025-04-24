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
    
# -------------- Memoization --------------
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

# -------------- Tabulation --------------
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for j in range(n)] for i in range(m)]
        
        # There is only one way to reach from start to start
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                    
                up = dp[i-1][j] if i-1 >= 0 else 0
                left = dp[i][j-1] if j-1 >= 0 else 0

                dp[i][j] = up + left
        
        return dp[-1][-1]

# -------------- Space Optimization --------------
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        """
        Initially we know that
            * First row will hold all 1's
            * First column will hold all 1's
        """

        for i in range(1, m):
            for j in range(1, n):
                up = dp[j]
                left = dp[j-1]

                # replace the value at current position
                dp[j] = up + left
        
        return dp[-1]