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

        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, n+1):
                ## Match
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    # No Match
                    split_1 = 0 + dp[i-1][j]
                    split_2 = 0 + dp[i][j-1]

                    dp[i][j] = max(split_1, split_2)
        
        return dp[n][n]