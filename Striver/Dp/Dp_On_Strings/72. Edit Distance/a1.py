# --------------------- Recursion Solution ---------------------

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        i = m - 1
        j = n - 1

        return self.recursion(i, j, word1, word2)
    
    def recursion(self, i, j, s1, s2):
        # base case
        if i < 0 and j < 0:
            # When everything matched perfectly
            return 0

        if j < 0:
            # delete elements from word1 as word2 is 0
            return i + 1
        
        if i < 0:
            # Insert element in word1 to match word2
            return j + 1
        
        # Logic
        if s1[i] == s2[j]:
            # There is a match, no operation needed
            return self.recursion(i - 1, j - 1, s1, s2)
        else:
            delete = self.recursion(i - 1, j, s1, s2)
            replace = self.recursion(i - 1, j - 1, s1, s2)
            insert = self.recursion(i, j - 1, s1, s2)

            return 1 + min(delete, replace, insert)

# ------------------ Memoization Solution ------------------
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        i = m - 1
        j = n - 1

        memo = {}

        return self.recursion(i, j, memo, word1, word2)
    
    def recursion(self, i, j, memo, s1, s2):
        # base case
        if i < 0 and j < 0:
            # When everything matched perfectly
            return 0

        if j < 0:
            # delete elements from word1 as word2 is 0
            return i + 1
        
        if i < 0:
            # Insert element in word1 to match word2
            return j + 1
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        # Logic
        if s1[i] == s2[j]:
            # There is a match, no operation needed
            memo[(i, j)] = self.recursion(i - 1, j - 1, memo, s1, s2)

            return memo[(i, j)]
        else:
            delete = self.recursion(i - 1, j, memo, s1, s2)
            replace = self.recursion(i - 1, j - 1, memo, s1, s2)
            insert = self.recursion(i, j - 1, memo, s1, s2)

            memo[(i, j)] = 1 + min(delete, replace, insert)

            return memo[(i, j)]
        
# ------------------ Memoization Solution with 1 base index ------------------

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        i = m
        j = n

        memo = {}

        return self.recursion(i, j, memo, word1, word2)
    
    def recursion(self, i, j, memo, s1, s2):
        # base case
        if i == 0 and j == 0:
            # When everything matched perfectly
            return 0

        if j == 0:
            # delete elements from word1 as word2 is 0
            return i
        
        if i == 0:
            # Insert element in word1 to match word2
            return j
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        # Logic
        if s1[i-1] == s2[j-1]:
            # There is a match, no operation needed
            memo[(i, j)] = self.recursion(i - 1, j - 1, memo, s1, s2)

            return memo[(i, j)]
        else:
            delete = self.recursion(i - 1, j, memo, s1, s2)
            replace = self.recursion(i - 1, j - 1, memo, s1, s2)
            insert = self.recursion(i, j - 1, memo, s1, s2)

            memo[(i, j)] = 1 + min(delete, replace, insert)

            return memo[(i, j)]
        
# ------------------ Tabulation Solution ------------------
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
    
# ------------------ Space Optimized Tabulation Solution ------------------
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [0 for _ in range(n+1)]

        # base case
        dp[0] = 0

        # for i in range(1, m+1):
        #     dp[i][0] = i
        
        for j in range(1, n+1):
            dp[j] = j
        
        for i in range(1, m+1):
            temp = [0 for _ in range(n+1)]
            temp[0] = i

            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    # There is a match, no operation needed
                    temp[j] = dp[j-1]
                else:
                    insert = temp[j-1]
                    delete = dp[j]
                    replace = dp[j-1]

                    temp[j] = 1 + min(insert, delete, replace)

            dp = temp
        
        return dp[n]