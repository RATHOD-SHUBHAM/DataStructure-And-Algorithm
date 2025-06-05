class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1 = s
        s2 = s[::-1] # reverse of s

        return self.LCS(s1, s2)
    
    def LCS(self, s1, s2):
        n = len(s1)

        dp = [[0 for _ in range(n+1)]for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, n+1):
                # Match
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    split_1 = dp[i-1][j]
                    split_2 = dp[i][j-1]
                    dp[i][j] = max(split_1, split_2)
        
        return dp[n][n]