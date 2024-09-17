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