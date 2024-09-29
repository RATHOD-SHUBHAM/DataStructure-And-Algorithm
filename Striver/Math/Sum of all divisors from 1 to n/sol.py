import math
class Solution:
    def factor_n(self, N):
        factors = 0
        sqrt_n = math.floor(math.sqrt(N))
        
        for i in range(1, sqrt_n + 1):
            if (N % i) == 0:
                factors += i
                
                if (N // i) != i:
                    factors += (N // i)
        
        return factors
                    
    def sumOfDivisors(self, N):
        sum_of_all_factors = 0
        
        for x in range(1, N+1):
            sum_of_all_factors += self.factor_n(x)
        
        return sum_of_all_factors