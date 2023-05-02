# TC: O(2^n) | Sc: O(n * m)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        i = len(text1) - 1
        j = len(text2) - 1
        
        return self.LCS(i, j, text1, text2)
    
    def LCS(self, i, j, s1, s2):
        # base case
        if i < 0 or j < 0:
            return 0
        
        # code
        # match
        if s1[i] == s2[j]:
            return 1 + self.LCS(i-1, j-1, s1, s2)
        
        return max(self.LCS(i, j-1, s1, s2), self.LCS(i-1, j, s1, s2))