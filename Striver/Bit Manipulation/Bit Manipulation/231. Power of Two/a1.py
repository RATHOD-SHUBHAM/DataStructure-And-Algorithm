# ----------------- Brute Force -----------------

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        
        # if the number is not divisible by 2, we will get a float value
        while n % 2 == 0:
            n = n / 2
        
        # if a number is divisible by 2 - the last remaining value will be 1
        return n == 1
    

# ----------------- Set bit -----------------
# Set bit: numbers divisible by 2 will only have a single 1 in their binary representation.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        
        count = 0
        x = 1

        while x <= n:
            if (n & x) >= 1:
                count += 1
            
            x = x << 1
        
        return count == 1
    

# ----------------- Right Shift -----------------

# Right Shift: numbers divisible by 2 will only have a single 1 in their binary representation.

import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        
        while n >= 1:
            if n & 1 == 0:
                n = n >> 1
            else:
                break

        return n == 1
    

# ----------------- And operation -----------------

'''
And operation between multiple of 2 and next lower number will always give 0 and other wise it will never be 0.

example 1: 8 & 7
1000(8) & 0111(7) => 0000(0)

example 1: = 10 & 9
1010(10) & 1001(9) => 1000(8)
'''

import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        
        return n & (n - 1) == 0