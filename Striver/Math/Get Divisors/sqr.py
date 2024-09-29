'''
36

1 x 36
2 x 18
3 x 12
4 x 9
6 x 6

'''

import math
class Solution:
    def sumOfDivisors(self, N):
        factors = 0

        for i in range(1, math.floor(math.sqrt(N)) + 1):
            if (N % i) == 0:
                factors += i
                
                if (N // i ) != i:
                    factors += (N // i )

        return factors