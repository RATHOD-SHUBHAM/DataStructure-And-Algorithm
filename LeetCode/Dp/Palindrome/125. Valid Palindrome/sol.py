class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        
        if n <= 1:
            return True
        
        s = s.lower()
        
        
        left = 0
        right = n - 1
        
        while left < right:
            # skip the alphanumeric character
            while left < right and not self.isAlpha(s[left]):
                left += 1
            
            while left < right and not self.isAlpha(s[right]):
                right -= 1
                
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
            
        return True
        
    def isAlpha(self, c):
        if (
            ord('a') <= ord(c) <= ord('z')
            or
            ord('0') <= ord(c) <= ord('9')
        ):
            return True # true if this is a alpha nuumeric character
        else:
            return False # False if this is not a alpha numeric character