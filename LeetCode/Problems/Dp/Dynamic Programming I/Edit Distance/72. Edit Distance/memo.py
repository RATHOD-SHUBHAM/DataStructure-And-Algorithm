# recursion
# Tc: O(n + m) | Sc= O(n + m) + O(n + m)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_w1 = len(word1)
        len_w2 = len(word2)
        
        i = len_w1 - 1
        j = len_w2 - 1
        
        memo = [[None for _ in range(len_w2)]for _ in range(len_w1)]
        
        return self.backtrack(i , j, memo, word1, word2)
    
    def backtrack(self, i , j, memo, word1, word2):
        # base case
        if i < 0:
            return j - 0 + 1
        
        if j < 0:
            return i - 0 + 1
        
        if memo[i][j] is not None:
            return memo[i][j]
        
        if word1[i] == word2[j]:
            memo[i][j] = self.backtrack(i - 1 , j - 1, memo, word1, word2)
            return memo[i][j]
            
        memo[i][j] =  1 + min(
            self.backtrack(i , j - 1, memo, word1, word2),
            self.backtrack(i - 1 , j , memo, word1, word2),
            self.backtrack(i - 1 , j - 1, memo, word1, word2)
        )
        
        return memo[i][j]
            