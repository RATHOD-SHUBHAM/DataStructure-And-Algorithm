# recursion
# Tc: O(2^ (n + m))
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_w1 = len(word1)
        len_w2 = len(word2)
        
        i = len_w1 - 1
        j = len_w2 - 1
        
        return self.backtrack(i , j, word1, word2)
    
    def backtrack(self, i , j, word1, word2):
        # base case
        if i < 0:
            return j - 0 + 1
        
        if j < 0:
            return i - 0 + 1
        
        if word1[i] == word2[j]:
            return self.backtrack(i - 1 , j - 1, word1, word2)
            
        return 1 + min(
            self.backtrack(i , j - 1, word1, word2),
            self.backtrack(i - 1 , j , word1, word2),
            self.backtrack(i - 1 , j - 1, word1, word2)
        )
            