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
    
# -------------------- Memoization --------------------
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

        memo = {}

        return self.recursion(idx_1, idx_2, memo, s1, s2)
    
    def recursion(self, idx_1, idx_2, memo, s1, s2):
        # Base Case
        if idx_1 < 0 or idx_2 < 0:
            return 0
        
        # Logic
        ## Match
        if s1[idx_1] == s2[idx_2]:
            return 1 + self.recursion(idx_1 - 1, idx_2 - 1, memo, s1, s2)
        
        # No Match
        split_1 = 0 + self.recursion(idx_1 - 1, idx_2, memo, s1, s2)
        split_2 = 0 + self.recursion(idx_1, idx_2 - 1, memo, s1, s2)

        return max(split_1, split_2)
    
# -------------------- Tabulation --------------------

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

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                ## Match
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    # No Match
                    split_1 = 0 + dp[i-1][j]
                    split_2 = 0 + dp[i][j-1]

                    dp[i][j] = max(split_1, split_2)
        
        return dp[m][n]

# -------------------- Space Optimized --------------------

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

        dp = [0 for _ in range(n+1)]

        for i in range(1, m+1):
            temp = [0 for _ in range(n+1)]

            for j in range(1, n+1):
                ## Match
                if s1[i - 1] == s2[j - 1]:
                    temp[j] = 1 + dp[j-1]
                else:
                    # No Match
                    split_1 = 0 + dp[j]
                    split_2 = 0 + temp[j-1]

                    temp[j] = max(split_1, split_2)
            
            dp = temp
        
        return dp[n]
