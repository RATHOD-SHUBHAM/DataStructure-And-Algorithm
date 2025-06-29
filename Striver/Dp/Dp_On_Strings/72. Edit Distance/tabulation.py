class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[0 for _ in range(n+1)]for _ in range(m+1)]

        # base case
        """
        In your DP table

        You set up dp of size (m+1)×(n+1) where row i means “using the first i characters of word1” (i.e. word1[:i]), and column j means “into the first j characters of word2” (word2[:j]).

        So dp[i][0] is “turn word1[:i] into the empty string” → that’s delete i times, not i+1.

        And dp[0][j] is “turn the empty string into word2[:j]” → that’s insert j times.
        """
        for i in range(m+1):
            # Minimum opertation to convert s1 to s2, will be to delete element in s1
            dp[i][0] = i
        
        for j in range(n+1):
            # Minimum opertation to convert s1 to s2, will be to insert element in s1
            dp[0][j] = j
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                # Logic
                if word1[i-1] == word2[j-1]:
                    # There is a match, no operation needed
                    dp[i][j] = dp[i-1][j-1]
                else:
                    delete = dp[i-1][j]
                    replace = dp[i-1][j-1]
                    insert = dp[i][j-1]

                    dp[i][j] = 1 + min(delete, replace, insert)
        
        return dp[m][n]