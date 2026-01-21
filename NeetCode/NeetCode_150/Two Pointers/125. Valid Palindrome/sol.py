class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)

        s = s.lower()

        right = n-1
        left = 0

        while left <= right:
            while left < n and s[left].isalnum() == False:
                left += 1
            
            while right >= 0 and s[right].isalnum() == False:
                right -= 1
            
            # Check if the index are still in range
            if left >= n or right < 0:
                break
            
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
            
        
        return True
        