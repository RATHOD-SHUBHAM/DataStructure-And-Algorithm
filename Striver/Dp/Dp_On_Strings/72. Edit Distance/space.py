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