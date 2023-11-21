# Brute Force ------------------------------------------------------------------------------

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True 

        reversed_s = s[::-1]
        # print(reversed_s)

        lower_s = s.lower()
        # print(lower_s)
        lower_reversed_s = reversed_s.lower()
        # print(lower_reversed_s)

        n = len(lower_s)
        # print(n)
        
        i = 0
        j = 0

        while i < n and j < n:
            while i < n and not lower_s[i].isalnum():
                i += 1
            
            while j < n and not lower_reversed_s[j].isalnum():
                j += 1

            
            if i >= n or j >= n:
                break

            # print(lower_s[i] , lower_reversed_s[j])

            if lower_s[i] != lower_reversed_s[j]:
                return False
            
            i += 1
            j += 1
        
        return True

# 2 Pointer ------------------------------------------------------------------------------

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