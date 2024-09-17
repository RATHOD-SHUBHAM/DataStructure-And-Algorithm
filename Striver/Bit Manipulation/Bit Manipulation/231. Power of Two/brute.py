# Brute Force

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        
        # if the number is not divisible by 2, we will get a float value
        while n % 2 == 0:
            n = n / 2
        
        # if a number is divisible by 2 - the last remaining value will be 1
        return n == 1
        