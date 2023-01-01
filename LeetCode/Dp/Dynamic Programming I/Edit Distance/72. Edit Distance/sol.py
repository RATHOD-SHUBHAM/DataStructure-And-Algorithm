# tabulation
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_w1 = len(word1)
        len_w2 = len(word2)
        
        dp = [[0 for _ in range(len_w2 + 1)] for _ in range(len_w1 + 1)]
        
        # last row
        for i in range(len_w2):
            dp[-1][i] = len_w2 - i
        

        # last col
        for j in range(len_w1):
            dp[j][-1] = len_w1 - j
        
        # print(dp)
        
        for i in reversed(range(len_w1)):
            for j in reversed(range(len_w2)):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1] # substring value
                else:
                    dp[i][j] = 1 + min(dp[i][j + 1] , dp[i + 1][j], dp[i+1][j+1])
                    
        return dp[0][0]
                    
            