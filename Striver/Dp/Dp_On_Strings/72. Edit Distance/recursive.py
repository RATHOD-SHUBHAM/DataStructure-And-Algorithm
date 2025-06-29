class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        i = m - 1
        j = n - 1

        return self.recursion(i, j, word1, word2)
    
    def recursion(self, i, j, s1, s2):
        # base case
        if j < 0:
            # Minimum opertation to convert s1 to s2, will be to delete element in s1
            return i + 1 # No of elements to delete
        
        if i < 0:
            # Minimum opertation to convert s1 to s2, will be to insert element in s1
            return j + 1 # No of elements to insert
        
        # Logic
        if s1[i] == s2[j]:
            # There is a match, no operation needed
            return self.recursion(i - 1, j - 1, s1, s2)
        else:
            delete = self.recursion(i - 1, j, s1, s2)
            replace = self.recursion(i - 1, j - 1, s1, s2)
            insert = self.recursion(i, j - 1, s1, s2)

            return 1 + min(delete, replace, insert)