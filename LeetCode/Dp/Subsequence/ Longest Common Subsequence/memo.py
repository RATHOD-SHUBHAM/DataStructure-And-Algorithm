# TC: O(n * m) | Sc: O(n * m) + O(n + m)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        
        i = m - 1
        j = n - 1
        
        memo = [[None for _ in range(n)] for _ in range(m)]
        
        return self.LCS(i, j, memo, text1, text2)
    
    def LCS(self, i, j, memo, s1, s2):
        # base case
        if i < 0 or j < 0:
            return 0
        
        if memo[i][j]:
            return memo[i][j]
        
        # code
        # match
        if s1[i] == s2[j]:
            memo[i][j] = 1 + self.LCS(i-1, j-1, memo, s1, s2)
        else:
            memo[i][j] = max(self.LCS(i, j-1, memo, s1, s2), self.LCS(i-1, j, memo, s1, s2))
            
        return memo[i][j]