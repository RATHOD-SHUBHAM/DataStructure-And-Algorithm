class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1 = s
        s2 = s[::-1] # reverse of s

        return self.LCS(s1, s2)
    
    def LCS(self, s1, s2):
        n = len(s1)

        dp = [0 for _ in range(n+1)]

        for i in range(1, n+1):
            temp = [0 for _ in range(n+1)]
            for j in range(1, n+1):
                # Match
                if s1[i-1] == s2[j-1]:
                    temp[j] = 1 + dp[j-1]
                else:
                    split_1 = dp[j]
                    split_2 = temp[j-1]
                    temp[j] = max(split_1, split_2)
            
            dp = temp
        
        return dp[n]