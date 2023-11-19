# Tc: O(n) and SC: O(1)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s[left + 1  : right + 1]) or self.isPalindrome(s[left : right])
            
            left += 1
            right -= 1
            
        return True
                
        
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
            
        return True