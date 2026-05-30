# Tc: O(n) | Sc: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        
        s = s.lower()

        left = 0
        right = n - 1

        while left < right:
            # Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Now we are sure this is a valid character
            # compare and see if they are valid palindrome
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        
        return True