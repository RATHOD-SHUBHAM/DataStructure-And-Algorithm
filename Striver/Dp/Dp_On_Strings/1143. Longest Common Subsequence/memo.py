# Tc : O(m * n)
# Sc : O(m * n) + O(m + n) for recursion stack space

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        idx1 = m - 1
        idx2 = n - 1

        memo = {}

        return self.recursion(idx1, idx2, memo, text1, text2)
    
    def recursion(self, idx1, idx2, memo, text1, text2):
        # base case
        if idx1 < 0 or idx2 < 0:
            return 0
        
        if (idx1, idx2) in memo:
            return memo[(idx1, idx2)]
        
        # Logic
        # Match: When the character matches
        if text1[idx1] == text2[idx2]:
            memo[(idx1, idx2)] = 1 + self.recursion(idx1 - 1, idx2 - 1, memo, text1, text2)
            return memo[(idx1, idx2)]
        
        # No Match: When the character doesnot matches
        split_1 = 0 + self.recursion(idx1 - 1, idx2, memo, text1, text2)
        split_2 = 0 + self.recursion(idx1, idx2 - 1, memo, text1, text2)

        memo[(idx1, idx2)] = max(split_1, split_2)

        return memo[(idx1, idx2)]