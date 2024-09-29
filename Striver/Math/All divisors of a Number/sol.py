import math

class Solution:
    def print_divisors(self, N):
        factors = []
        sqrt_N = math.floor(math.sqrt(N))
        
        for i in range(1, sqrt_N + 1):
            if N % i == 0:
                factors.append(i)
                
                if (N//i) != i:
                    factors.append(N//i)
        
        factors.sort()
        for num in factors:
            print(num, end=' ')