class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        dp = [0 for _ in range(n+1)]

        # base case
        # i < 0 and j < 0 -> True
        dp[0] = True

        # j < 0 and i >= 0
        # for i in range(1, m+1):
            # dp[i][0] = False

        # i < 0 and j >= 0
        for j in range(1, n+1):
            flag = True
            for x in range(j):
                # We need to check if pattern is all * -> because * can be matched to empty string
                if p[x] != '*':
                    flag = False
            
            dp[j] = flag
        
        # Logic
        for i in range(1, m+1):
            temp = [0 for _ in range(n+1)]
            """
            # j < 0 and i >= 0
            for i in range(1, m+1):
                dp[i][0] = False
            """
            temp[0] = False

            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    # if the character matched, or we used ? to match single character
                    temp[j] = dp[j-1]
                
                elif p[j-1] == '*':
                    # Wildcard match
                    # Consider * = "" -> so we move forward
                    split_1 = temp[j-1]

                    # Consider * = character at s[i]
                    split_2 = dp[j]
                    # We dont move j-1 because we can match any number of character - so keep * to match with upcoming characters

                    temp[j] = split_1 or split_2
                
                else:
                    # Characters didnt match
                    temp[j] = False

            dp = temp
        
        return dp[n]