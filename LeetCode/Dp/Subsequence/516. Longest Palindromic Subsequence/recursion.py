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