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
        