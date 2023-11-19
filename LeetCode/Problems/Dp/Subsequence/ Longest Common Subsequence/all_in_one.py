# ----------------------- Recursion --------------------------------------------

# TC: O(2^n) | Sc: O(n * m)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        i = len(text1) - 1
        j = len(text2) - 1
        
        return self.LCS(i, j, text1, text2)
    
    def LCS(self, i, j, s1, s2):
        # base case
        if i < 0 or j < 0:
            return 0
        
        # code
        # match
        if s1[i] == s2[j]:
            return 1 + self.LCS(i-1, j-1, s1, s2)
        
        return max(self.LCS(i, j-1, s1, s2), self.LCS(i-1, j, s1, s2))
    

# ----------------------- Memoization --------------------------------------------

# TC: O(n * m) | Sc: O(n * m) + O(n + m)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        
        i = m - 1
        j = n - 1
        
        memo = [[None for _ in range(n)] for _ in range(m)]
        
        return self.LCS(i, j, memo, text1, text2)
    
    def LCS(self, i, j, memo, s1, s2):
        # base case
        if i < 0 or j < 0:
            return 0
        
        if memo[i][j]:
            return memo[i][j]
        
        # code
        # match
        if s1[i] == s2[j]:
            memo[i][j] = 1 + self.LCS(i-1, j-1, memo, s1, s2)
        else:
            memo[i][j] = max(self.LCS(i, j-1, memo, s1, s2), self.LCS(i-1, j, memo, s1, s2))
            
        return memo[i][j]
    

# ----------------------- dp --------------------------------------------

# TC: O(n * m) | Sc: O(n * m)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                    
        return dp[-1][-1]
    
# ----------------------- dp with subsequence --------------------------------------------

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # recursion
        m = len(text1)
        n = len(text2)
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(1, m +1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1] , dp[i-1][j])
        
        self.buildSubsequence(text1, text2, dp)
        return dp[-1][-1]
    
    def buildSubsequence(self, text1, text2, dp):
        m = len(text1)
        n = len(text2)
        
        i = m
        j = n 
        
        subsequence = []
        
        while i > 0 and j > 0:
            # if string match
            if text1[i-1] == text2[j-1]:
                subsequence.append(text1[i-1])
                i -= 1
                j -= 1
            # if the string dont match - move left or top
            elif dp[i][j-1] > dp[i-1][j]:
                j -= 1
            else:
                i -= 1
        
        sub = "".join(subsequence[::-1])
        print(sub)




# ----------------------- Space Optimized --------------------------------------------

# TC: O(n * m) | Sc: O(n)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        
        prev = [0 for _ in range(n + 1)]
        cur = [0 for _ in range(n + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n+1):
                if(text1[i-1] == text2[j-1]):
                    cur[j] = 1 + prev[j-1]
                else:
                    cur[j] = max(prev[j],cur[j-1]) 
        
            prev = [x for x in cur]
            # prev = cur -  this will change the value in prev as well if i change something in cur
        
        return prev[-1] 