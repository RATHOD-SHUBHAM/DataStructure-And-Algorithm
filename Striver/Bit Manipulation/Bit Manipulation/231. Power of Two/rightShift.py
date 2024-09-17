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