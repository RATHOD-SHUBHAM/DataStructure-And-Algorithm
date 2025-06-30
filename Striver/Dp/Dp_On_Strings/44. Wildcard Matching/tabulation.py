"""
What Each Cell Represents:

    * dp[i][j] = whether the first i characters of string s can match the first j characters of pattern p
    * The bottom-right cell dp[m][n] gives the final answer
    * Base cases are handled for empty strings and patterns with only *
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        dp = [[0 for _ in range(n+1)]for _ in range(m+1)]

        # base case
        # i < 0 and j < 0 -> True
        dp[0][0] = True

        # j < 0 and i >= 0
        for i in range(1, m+1):
            dp[i][0] = False

        # i < 0 and j >= 0
        for j in range(1, n+1):
            flag = True
            for x in range(j):
                # We need to check if pattern is all * -> because * can be matched to empty string
                if p[x] != '*':
                    flag = False
            
            dp[0][j] = flag
        
        # Logic
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    # if the character matched, or we used ? to match single character
                    dp[i][j] = dp[i-1][j-1]
                
                elif p[j-1] == '*':
                    # Wildcard match
                    # Consider * = "" -> so we move forward
                    split_1 = dp[i][j-1]

                    # Consider * = character at s[i]
                    split_2 = dp[i-1][j]
                    # We dont move j-1 because we can match any number of character - so keep * to match with upcoming characters

                    dp[i][j] = split_1 or split_2
                
                else:
                    # Characters didnt match
                    dp[i][j] = False
        
        return dp[m][n]