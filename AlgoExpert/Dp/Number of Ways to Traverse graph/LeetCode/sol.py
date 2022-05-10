#Time and Space = O(m + n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # create a extra layer of zero on top and right to handle list index out of bounce
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i == 1 and j == 1:
                    dp[i][j] = 1
                else:
                    ways_To_reach_UpperCell = dp[i-1][j]
                    ways_To_reach_LeftCell = dp[i][j-1]
                    dp[i][j] = ways_To_reach_UpperCell + ways_To_reach_LeftCell
        
        return dp[m][n]
                