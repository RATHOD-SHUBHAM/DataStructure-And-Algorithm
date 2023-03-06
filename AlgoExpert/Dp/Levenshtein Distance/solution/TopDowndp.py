# leetcode question 72: Edit distance
# time and space = O(mn)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_word1 = len(word1)
        len_word2 = len(word2)
        
        if len_word1 == 0:
            return len_word2
        
        if len_word2 == 0:
            return len_word1
        
        
        dp = [[None for _ in range(len_word2 + 1)]for _ in range(len_word1 + 1)]
        
        # fill last col
        for row in range(len_word1 + 1):
            dp[row][len_word2] = len_word1 - row
            
        # filling last row
        for col in range(len_word2 + 1):
            dp[len_word1][col] = len_word2 - col
            
        # dp - top down
        for i in reversed(range(len_word1)):
            for j in reversed(range(len_word2)):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
					# 1 + compare remaining elements
                    dp[i][j] = 1 + min(
                        dp[i+1][j+1],
                        dp[i+1][j],
                        dp[i][j+1]
                    )
                    
                    
        return dp[0][0]