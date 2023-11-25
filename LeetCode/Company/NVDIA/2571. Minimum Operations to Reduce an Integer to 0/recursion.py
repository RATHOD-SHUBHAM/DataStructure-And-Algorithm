'''
Bits are: 64 32 16 8 4 2 1
    
    
    n = 39

    we want to subtract n with a bit more than n,
    also 
    subtract a bit from n which is less that n.

    eg 64 - 39 and 39 - 32



'''

class Solution:
    def minOperations(self, n: int) -> int:
        if n <= 1:
            return n
        
        # Get the val - power of 2 - which is less than n
        val = 1
        while val * 2 < n:
            # we multiply by 2 becaues we want power of 2
            val = val * 2
        # print(val)
        
        # present operation + minimum of other operation
        return 1 + min(self.minOperations(n - val), self.minOperations((val*2) - n))