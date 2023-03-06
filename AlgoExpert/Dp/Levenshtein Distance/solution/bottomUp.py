class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_word1 = len(word1)
        len_word2 = len(word2)
        
        if len_word1 == 0:
            return len_word2
        
        if len_word2 == 0:
            return len_word1
        
        
        dp = [[None for _ in range(len_word2 + 1)]for _ in range(len_word1 + 1)]
        
        # fill the row 0
        # if there is no element in word1 and n element in word2 . then we need n distance to convert word1 to word2
        for col in range(len_word2 + 1):
            dp[0][col] = col
            
        # fill col 0
        for row in range(len_word1 + 1):
            dp[row][0] = row
            
        #dp
        for i in range(1, len_word1 + 1):
            for j in range(1, len_word2 + 1):
                # -1 because 0 indexed
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 1 + compare remaining elements
                    dp[i][j] = 1 + min(
                        dp[i][j-1],
                        dp[i-1][j],
                        dp[i-1][j-1]
                    )
                    
        return dp[-1][-1]