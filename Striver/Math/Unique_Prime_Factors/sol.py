import math
class Solution:
    def isPrime(self, N):
        if N > 1 and N < 4:
            return True
            
        sqrt_n = math.floor(math.sqrt(N))
        
        count = 0
        for i in range(1, sqrt_n + 1):
            if N % i == 0:
                count += 1
                if (N // i) != i:
                    count += 1
        
        if count == 2:
            return True
        else:
            return False
                    
    def get_factors(self, N):
        sqrt_n = math.floor(math.sqrt(N))
        unique_factor = []
        
        for i in range(1, sqrt_n + 1):
            if N % i == 0:
                if self.isPrime(i) == True:
                    unique_factor.append(i)
                
                
                if (N // i) != i:
                    if self.isPrime(N // i) == True:
                        unique_factor.append(N // i)
        
        return unique_factor
            
    def AllPrimeFactors(self, N):
        # Prime factor of N
        factor = self.get_factors(N)
        factor.sort()
        return factor