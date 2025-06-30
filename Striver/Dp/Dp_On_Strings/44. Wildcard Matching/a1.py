# -------------------------- Recursion Solution --------------------------

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        i = m - 1
        j = n - 1

        return self.recursion(i, j, s, p)
    
    def recursion(self, i, j, s, p):
        # base case
        if i < 0 and j < 0:
            # when both string and pattern matched completely
            return True
        
        if j < 0 and i >= 0:
            # When there is some string remaining but pattern got exhausted
            return False
        
        if i < 0:
            # When string is complete
            for x in range(j+1):
                # We need to check if pattern is all * -> because * can be matched to empty string
                if p[x] != '*':  # Changed from p[j] to p[x]
                    return False
            
            return True
        
        # Logic
        if s[i] == p[j] or p[j] == '?':
            # if the character matched, or we used ? to match single character
            return self.recursion(i - 1, j - 1, s, p)
        
        elif p[j] == '*':
            # Wildcard match
            # Consider * = "" -> so we move forward
            split_1 = self.recursion(i, j-1, s, p)

            # Consider * = character at s[i]
            split_2 = self.recursion(i-1, j, s, p)
            # We dont move j-1 because we can match any number of character - so keep * to match with upcoming characters

            return split_1 or split_2
        
        else:
            # Characters didnt match
            return False

# ---------------------------- Memoization Solution ----------------------------
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        i = m - 1
        j = n - 1

        memo = {}

        return self.recursion(i, j, memo, s, p)
    
    def recursion(self, i, j, memo, s, p):
        # base case
        if i < 0 and j < 0:
            # when both string and pattern matched completely
            return True
        
        if j < 0 and i >= 0:
            # When there is some string remaining but pattern got exhausted
            return False
        
        if i < 0:
            # When string is complete
            for x in range(j+1):
                # We need to check if pattern is all * -> because * can be matched to empty string
                if p[x] != '*':  # Changed from p[j] to p[x]
                    return False
            
            return True
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        # Logic
        if s[i] == p[j] or p[j] == '?':
            # if the character matched, or we used ? to match single character
            memo[(i, j)] = self.recursion(i - 1, j - 1, memo, s, p)
            return memo[(i, j)]
        
        elif p[j] == '*':
            # Wildcard match
            # Consider * = "" -> so we move forward
            split_1 = self.recursion(i, j-1, memo, s, p)

            # Consider * = character at s[i]
            split_2 = self.recursion(i-1, j, memo, s, p)
            # We dont move j-1 because we can match any number of character - so keep * to match with upcoming characters

            memo[(i, j)] = split_1 or split_2
            return memo[(i, j)]
        
        else:
            # Characters didnt match
            memo[(i, j)] = False
            return memo[(i, j)]
        
# ---------------------------- Converting to 1 based indexing ----------------------------
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        i = m
        j = n

        memo = {}

        return self.recursion(i, j, memo, s, p)
    
    def recursion(self, i, j, memo, s, p):
        # base case
        if i == 0 and j == 0:
            # when both string and pattern matched completely
            return True
        
        if j == 0 and i > 0:
            # When there is some string remaining but pattern got exhausted
            return False
        
        if i == 0:
            # When string is complete
            for x in range(j):
                # We need to check if pattern is all * -> because * can be matched to empty string
                if p[x] != '*':  # Changed from p[j] to p[x]
                    return False
            
            return True
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        # Logic
        if s[i-1] == p[j-1] or p[j-1] == '?':
            # if the character matched, or we used ? to match single character
            memo[(i, j)] = self.recursion(i - 1, j - 1, memo, s, p)
            return memo[(i, j)]
        
        elif p[j-1] == '*':
            # Wildcard match
            # Consider * = "" -> so we move forward
            split_1 = self.recursion(i, j-1, memo, s, p)

            # Consider * = character at s[i]
            split_2 = self.recursion(i-1, j, memo, s, p)
            # We dont move j-1 because we can match any number of character - so keep * to match with upcoming characters

            memo[(i, j)] = split_1 or split_2
            return memo[(i, j)]
        
        else:
            # Characters didnt match
            memo[(i, j)] = False
            return memo[(i, j)]

# ---------------------------- Tabulation Solution ----------------------------

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

# ---------------------------- Space Optimized Tabulation Solution ----------------------------
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