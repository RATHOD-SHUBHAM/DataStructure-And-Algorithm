class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        m = len(S1)
        n = len(S2)
        
        i = m - 1
        j = n - 1
        
        count = 0
        
        return self.LC_substring(i , j, count, S1, S2)
        
    def LC_substring(self, i , j , count, s1, s2):
        # base case
        if i < 0 or j < 0:
            return count
            
        # code
        if s1[i] == s2[j]:
            return self.LC_substring(i - 1 , j - 1, count + 1, s1, s2)
        
        return max(
            self.LC_substring(i - 1 , j, 0, s1, s2),
            self.LC_substring(i, j - 1, 0, s1, s2)
            )