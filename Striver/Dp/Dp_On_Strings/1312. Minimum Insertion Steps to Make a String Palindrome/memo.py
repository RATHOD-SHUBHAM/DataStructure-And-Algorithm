class Solution:
    def minInsertions(self, s: str) -> int:
        """
        1. Find Longest Palindromic subsequence
        2. Check the remaining value and return that
        """

        s1 = s
        s2 = s[::-1]

        common_subseq_count = self.LPS(s1, s2)

        return len(s) - common_subseq_count
    
    def LPS(self, s1, s2):
        n = len(s2)

        idx_1 = n - 1
        idx_2 = n - 1

        memo = {}

        return self.recursion(idx_1, idx_2, memo, s1, s2)
    
    def recursion(self, idx_1, idx_2, memo, s1, s2):
        # Base Case
        if idx_1 < 0 or idx_2 < 0:
            return 0
        
        if (idx_1, idx_2) in memo:
            return memo[(idx_1, idx_2)]
        
        # Logic
        ## Match
        if s1[idx_1] == s2[idx_2]:
            return 1 + self.recursion(idx_1 - 1, idx_2 - 1, memo, s1, s2)
        
        # No Match
        split_1 = 0 + self.recursion(idx_1 - 1, idx_2, memo, s1, s2)
        split_2 = 0 + self.recursion(idx_1, idx_2 - 1, memo, s1, s2)

        memo[(idx_1, idx_2)] = max(split_1, split_2)

        return memo[(idx_1, idx_2)]

