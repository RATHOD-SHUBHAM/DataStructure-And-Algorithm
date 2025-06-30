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