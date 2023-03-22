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