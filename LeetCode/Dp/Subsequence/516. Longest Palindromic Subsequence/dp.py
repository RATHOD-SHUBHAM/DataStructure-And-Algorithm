# Tc: O(n^2) | O(n^2)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        m = len(s)
        
        # the catch here is if we write the string in reverse order and compare the original and reversed string. We will get the LCS which will eventually be the LPS
        rs = s[ : : -1]
        
        n = len(rs)
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == rs[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                    
        return dp[-1][-1]