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