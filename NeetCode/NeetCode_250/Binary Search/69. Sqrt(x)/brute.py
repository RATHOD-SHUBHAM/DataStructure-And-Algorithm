# The square root of x is the number that, multiplied by itself, gives x.
# k * k = x, in our case we have to round it down so k * k <= x

class Solution:
    def mySqrt(self, x: int) -> int:
        k = 0
        # Check if k hold number that works for k * k <= x
        while (k+1) * (k+1) <= x:
            k += 1
        
        return k