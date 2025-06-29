class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        # base case
        # Minimum opertation to convert s1 to s2, will be to insert element in s1
        # Insert i elements
        dp = [i for i in range(n+1)]
        
        for i in range(1, m+1):
            temp = [0 for _ in range(n+1)]
            temp[0] = i

            for j in range(1, n+1):
                # Logic
                if word1[i-1] == word2[j-1]:
                    # There is a match, no operation needed
                    temp[j] = dp[j-1]
                else:
                    delete = dp[j]
                    replace = dp[j-1]
                    insert = temp[j-1]

                    temp[j] = 1 + min(delete, replace, insert)
            
            dp = temp
        
        return dp[n]