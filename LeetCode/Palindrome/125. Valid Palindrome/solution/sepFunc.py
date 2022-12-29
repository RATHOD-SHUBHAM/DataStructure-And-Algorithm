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
            while left < right and not self.isAlphanumeric(lower_s[left]):
                left += 1
            
            while left < right and not self.isAlphanumeric(lower_s[right]):
                right -= 1
                
            if lower_s[left] != lower_s[right]:
                return False
            
            left += 1
            right -= 1
            
        return True
    
    def isAlphanumeric(self,char):
        # USING ASCII to check if the character is in btn the range
        if ( ord('a') <= ord(char) <= ord('z')
           or
           ord('0') <= ord(char) <= ord('9')):
            return True
        else:
            return False