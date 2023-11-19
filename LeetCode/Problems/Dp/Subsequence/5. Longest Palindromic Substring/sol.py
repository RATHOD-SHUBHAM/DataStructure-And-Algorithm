# Tc: O(n^2) | Sc: O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxLen = 0
        string = ""
        
        # odd length
        for i in range(n):
            left = i
            right = i

            length , substring = self.isPalindrome(left, right, s)

            if length > maxLen:
                string = substring
                maxLen = length
        
        # even length
        for i in range(n - 1):
            left = i
            right = i + 1

            length , substring = self.isPalindrome(left, right, s)

            if length > maxLen:
                string = substring
                maxLen = length
        
        return string
    
    def isPalindrome(self, left, right, s):
        n = len(s)
        length = 0
        res = ""
        
        while left >= 0 and right < n and s[left] == s[right]:
            new_length = right - left + 1
            
            if new_length > length:
                length = new_length
                res = s[left : right + 1]
            
            left -= 1
            right += 1
        
        return length, res