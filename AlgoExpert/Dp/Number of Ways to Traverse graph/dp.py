'''
										no of ways to reach the upper cell
No of ways to reach a particular cell = 	+
										no of ways to reach he left cell
'''
# Tc and Sc = O(m + n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None for _ in range(n)] for _ in range(m)]
        # print(dp)
        
        # there is one way to reach right or to left. so add one to 0th row and 0th col
        # fill the 0th row
        for col in range(n):
            dp[0][col] = 1
            
        # fill 0th col
        for row in range(m):
            dp[row][0] = 1
            
        # print(dp)
        
        for row in range(1, m):
            for col in range(1, n):
                # current cell = no of ways to reach from top and from left
                up = dp[row - 1][col]
                left = dp[row][col - 1]
                dp[row][col] = up + left
                
        return dp[-1][-1]