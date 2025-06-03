# -------------------------- Recursion --------------------------

# Tc: O(2^m * 2^n)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        idx1 = m - 1
        idx2 = n - 1

        return self.recursion(idx1, idx2, text1, text2)
    
    def recursion(self, idx1, idx2, text1, text2):
        # base case
        if idx1 < 0 or idx2 < 0:
            return 0
        
        # Logic
        # Match: When the character matches
        if text1[idx1] == text2[idx2]:
            return 1 + self.recursion(idx1 - 1, idx2 - 1, text1, text2)
        
        # No Match: When the character doesnot matches
        split_1 = 0 + self.recursion(idx1 - 1, idx2, text1, text2)
        split_2 = 0 + self.recursion(idx1, idx2 - 1, text1, text2)

        return max(split_1, split_2)
    
# -------------------------- Memoization --------------------------
# Tc : O(m * n)
# Sc : O(m * n) + O(m + n) for recursion stack space

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        idx1 = m - 1
        idx2 = n - 1

        memo = {}

        return self.recursion(idx1, idx2, memo, text1, text2)
    
    def recursion(self, idx1, idx2, memo, text1, text2):
        # base case
        if idx1 < 0 or idx2 < 0:
            return 0
        
        if (idx1, idx2) in memo:
            return memo[(idx1, idx2)]
        
        # Logic
        # Match: When the character matches
        if text1[idx1] == text2[idx2]:
            memo[(idx1, idx2)] = 1 + self.recursion(idx1 - 1, idx2 - 1, memo, text1, text2)
            return memo[(idx1, idx2)]
        
        # No Match: When the character doesnot matches
        split_1 = 0 + self.recursion(idx1 - 1, idx2, memo, text1, text2)
        split_2 = 0 + self.recursion(idx1, idx2 - 1, memo, text1, text2)

        memo[(idx1, idx2)] = max(split_1, split_2)

        return memo[(idx1, idx2)]

# -------------------------- Tabulation --------------------------
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        # since our base case has -1, lets add a extra layer in dp represent -1
        dp = [[0 for _ in range(n+1)]for _ in range(m+1)]

        # for i in range(m+1):
        #     dp[i][0] = 0
        
        # for j in range(n+1):
        #     dp[0][j] = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                # Match: When the character matches
                if text1[i-1] == text2[j-1]: # Our index is padded, inorder to correct it , we do -1
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    # No Match: When the character doesnot matches
                    split_1 = 0 + dp[i][j-1]
                    split_2 = 0 + dp[i-1][j]
                    dp[i][j] = max(split_1, split_2)
        
        return dp[m][n]

# -------------------------- Space Optimization --------------------------
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
