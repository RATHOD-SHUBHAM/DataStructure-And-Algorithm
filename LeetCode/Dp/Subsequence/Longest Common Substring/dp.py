class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        m = len(S1)
        n = len(S2)
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        res = 0
        
        for i in range(1, m + 1):
            for j in range(1 , n + 1):
                if S1[i - 1]== S2[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    res = max(res, dp[i][j])
                else:
                    dp[i][j] = 0
        

        return res