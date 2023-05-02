class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        m = len(S1)
        n = len(S2)
        
        i = m - 1
        j = n - 1
        
        count = 0
        
        memo = [[None for _ in range(n)] for _ in range(m)]
        
        return self.LC_substring(i , j, count, memo, S1, S2)
        
    def LC_substring(self, i , j , count, memo, s1, s2):
        # base case
        if i < 0 or j < 0:
            return count
        
        if memo[i][j]:
            return memo[i][j]
            
        # code
        if s1[i] == s2[j]:
            memo[i][j] = self.LC_substring(i - 1 , j - 1, count + 1, memo, s1, s2)
        else:
            memo[i][j] = max(
            self.LC_substring(i - 1 , j, 0, memo, s1, s2),
            self.LC_substring(i, j - 1, 0, memo, s1, s2)
            )
        
        return memo[i][j]