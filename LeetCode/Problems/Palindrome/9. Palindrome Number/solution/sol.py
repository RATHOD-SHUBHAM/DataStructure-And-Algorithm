# Tc: O(log(n)), Sc: O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # base case: negative number cannot be a palindorme
        if x < 0:
            return False
        
        # creating a copy of x
        copy_x = x
        
        # reverse the number
        reversed_x = 0
        while copy_x > 0:
            # get the last number
            rem = copy_x % 10
            
            # append the remainder
            reversed_x = reversed_x * 10 + rem
            
            # remove the last number from copy
            copy_x = copy_x // 10
            
        return reversed_x == x
        