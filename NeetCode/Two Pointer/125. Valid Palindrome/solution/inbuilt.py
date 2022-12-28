# TC: O(n) and SC: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        # convert the entire string to lower case
        lower_s = s.lower()
        
        while left < right:
            # if there is special character then skip
            # isalnum : check if it is alphabet or number
            while left < right and not lower_s[left].isalnum():
                left += 1
            
            while left < right and not lower_s[right].isalnum():
                right -= 1
                
            if lower_s[left] != lower_s[right]:
                return False
            
            left += 1
            right -= 1
            
        return True
                