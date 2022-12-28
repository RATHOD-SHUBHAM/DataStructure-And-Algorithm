class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        
        return str_x == reversed(str_x)