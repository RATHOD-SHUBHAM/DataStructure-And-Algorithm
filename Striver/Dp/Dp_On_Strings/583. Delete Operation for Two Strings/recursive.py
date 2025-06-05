class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        common_subseq_count = self.LCS(word1, word2)

        non_common_count_1 = len(word1) - common_subseq_count
        non_common_count_2 = len(word2) - common_subseq_count

        # return len(word1) - common_subseq_count + len(word2) - common_subseq_count
        return non_common_count_1 + non_common_count_2
    
    def LCS(self, s1, s2):
        m = len(s1)
        n = len(s2)

        idx_1 = m - 1
        idx_2 = n - 1

        return self.recursion(idx_1, idx_2, s1, s2)
    
    def recursion(self, idx_1, idx_2, s1, s2):
        # Base Case
        if idx_1 < 0 or idx_2 < 0:
            return 0
        
        # Logic
        ## Match
        if s1[idx_1] == s2[idx_2]:
            return 1 + self.recursion(idx_1 - 1, idx_2 - 1, s1, s2)
        
        # No Match
        split_1 = 0 + self.recursion(idx_1 - 1, idx_2, s1, s2)
        split_2 = 0 + self.recursion(idx_1, idx_2 - 1, s1, s2)

        return max(split_1, split_2)