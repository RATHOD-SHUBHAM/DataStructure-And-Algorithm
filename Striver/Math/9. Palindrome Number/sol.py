'''
Time complexity : O(log10(n))
We divided the input by 10 for every iteration, so the time complexity is O(log 
10(n))
Space complexity : O(1).
'''

class Solution:
    def reverseNumber(self, x):
        reversed_x = 0

        while x > 0:
            remainder = x % 10
            reversed_x = reversed_x * 10 + remainder
            x = x // 10
        
        return reversed_x
        
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        x = abs(x)
        reversed_x = self.reverseNumber(x)

        return x == reversed_x
        
        