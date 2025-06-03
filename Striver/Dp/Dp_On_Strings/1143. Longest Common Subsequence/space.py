class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        # since our base case has -1, lets add a extra layer in dp represent -1
        dp = [0 for _ in range(n+1)]

        # for i in range(m+1):
        #     dp[i][0] = 0
        
        # for j in range(n+1):
        #     dp[0][j] = 0

        for i in range(1, m+1):
            temp = [0 for _ in range(n+1)]
            for j in range(1, n+1):
                # Match: When the character matches
                if text1[i-1] == text2[j-1]: # Our index is padded, inorder to correct it , we do -1
                    temp[j] = 1 + dp[j-1]
                else:
                    # No Match: When the character doesnot matches
                    split_1 = 0 + temp[j-1]
                    split_2 = 0 + dp[j]
                    temp[j] = max(split_1, split_2)

            dp = temp
        
        return dp[n]
