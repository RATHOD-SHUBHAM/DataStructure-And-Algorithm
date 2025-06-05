class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1 = s
        s2 = s[::-1] # reverse of s


        return self.LCS(s1, s2)
    
    def LCS(self, s1, s2):
        n = len(s1)

        idx1 = n - 1
        idx2 = n - 1

        memo = {}

        return self.recursion(idx1, idx2, memo, s1, s2)

    def recursion(self, idx1, idx2, memo, s1, s2):
        # Base case
        if idx1 < 0 or idx2 < 0:
            return 0
        
        if (idx1, idx2) in memo:
            return memo[(idx1, idx2)]
        
        # Logic
        ## Match
        if s1[idx1] == s2[idx2]:
            return 1 + self.recursion(idx1-1, idx2-1, memo, s1, s2)
        
        ## No Match
        split_1 = 0 + self.recursion(idx1-1, idx2, memo, s1, s2)
        split_2 = 0 + self.recursion(idx1, idx2-1, memo, s1, s2)

        memo[(idx1, idx2)] = max(split_1, split_2)

        return memo[(idx1, idx2)]

