# Tc: O(2^m * 2^n)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        idx1 = m - 1
        idx2 = n - 1

        return self.recursion(idx1, idx2, text1, text2)
    
    def recursion(self, idx1, idx2, text1, text2):
        # base case
        if idx1 < 0 or idx2 < 0:
            return 0
        
        # Logic
        # Match: When the character matches
        if text1[idx1] == text2[idx2]:
            return 1 + self.recursion(idx1 - 1, idx2 - 1, text1, text2)
        
        # No Match: When the character doesnot matches
        split_1 = 0 + self.recursion(idx1 - 1, idx2, text1, text2)
        split_2 = 0 + self.recursion(idx1, idx2 - 1, text1, text2)

        return max(split_1, split_2)