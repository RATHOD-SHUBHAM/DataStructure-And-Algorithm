# -------------------------- Recursion -----------------------------------------

# Tc: O(2^n) | O(n)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        left = 0
        right = n - 1
        
        return self.LPS(left , right , s)
    
    def LPS(self, left, right, s):
        # base case
        if right < left:
            return 0
        
        if left == right:
            return 1
        
        # code
        if s[left] == s[right]:
            return 2 + self.LPS(left + 1 , right - 1, s)
        
        return max(
            self.LPS(left , right - 1, s) , 
            self.LPS(left + 1 , right, s)
        )
    

# -------------------------- Memo -----------------------------------------

# Tc: O(n^2) | O(n^2)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        left = 0
        right = n - 1
        
        memo = [[None for _ in range(n)] for _ in range(n)]
        
        return self.LPS(left , right , memo, s)
    
    def LPS(self, left, right, memo, s):
        # base case
        if right < left:
            return 0
        
        if left == right:
            return 1
        
        if memo[left][right]:
            return memo[left][right]
        
        # code
        if s[left] == s[right]:
            memo[left][right] = 2 + self.LPS(left + 1 , right - 1, memo, s)
        else:
            memo[left][right] = max(
            self.LPS(left , right - 1, memo, s) , 
            self.LPS(left + 1 , right, memo, s)
        )
        
        return memo[left][right]
    
# -------------------------- Dp -----------------------------------------

# Tc: O(n^2) | O(n^2)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        m = len(s)
        
        # the catch here is if we write the string in reverse order and compare the original and reversed string. We will get the LCS which will eventually be the LPS
        rs = s[ : : -1]
        
        n = len(rs)
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == rs[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                    
        return dp[-1][-1]
    

# -------------------------- Dp with sub -----------------------------------------

# Tc: O(n^2) | O(n^2)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        m = len(s)
        
        # the catch here is if we write the string in reverse order and compare the original and reversed string. We will get the LCS which will eventually be the LPS
        rs = s[ : : -1]
        
        n = len(rs)
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == rs[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                    
        self.buildSubsequence(dp , s, rs)
        return dp[-1][-1]
    
    def buildSubsequence(self, dp , s, rs):
        m = len(s)
        n = len(rs)
        
        subsequence = []
        
        i = m
        j = n
        
        while i > 0 and j > 0:
            if s[i-1] == rs[j-1]:
                subsequence.append(s[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
                
        subsequence = "".join(subsequence)
        print(subsequence)
        return subsequence
    

# -------------------------- space optimization -----------------------------------------

# Tc: O(n^2) | O(n)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        m = len(s)
        
        # the catch here is if we write the string in reverse order and compare the original and reversed string. We will get the LCS which will eventually be the LPS
        rs = s[ : : -1]

        
        prev = [0 for _ in range(m + 1)]
        cur = [0 for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, m + 1):
                if s[i - 1] == rs[j - 1]:
                    cur[j] = 1 + prev[j-1]
                else:
                    cur[j] = max(cur[j-1], prev[j])
                    
            prev = [x for x in cur]
                    
        return cur[-1]