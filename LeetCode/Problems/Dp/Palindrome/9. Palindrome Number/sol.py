class Solution:
    def isPalindrome(self, x: int) -> bool:
        copy_x = x
        
        reversed_x = 0
        
        while copy_x > 0:
            remainder = copy_x % 10
            
            reversed_x = reversed_x * 10 + remainder
            
            copy_x = copy_x // 10
            
        
        return reversed_x == x