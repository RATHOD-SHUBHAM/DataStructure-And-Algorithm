# Tc: O(n) | Sc: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        
        n = len(s)

        left = 0
        right = n - 1

        while left <= right:
            while left < n and not s[left].isalnum():
                left += 1
            
            while right >= 0 and not s[right].isalnum():
                right -= 1
            
            if left >= n or right < 0:
                break
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True