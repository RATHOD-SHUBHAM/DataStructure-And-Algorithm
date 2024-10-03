# -----------------------------------------------------------

# Find prime factorization of N

class Solution:
    def sieve(self, ref, N):
        # Smallest Sieve
        i = 2
        
        while i * i <= N:
            if ref[i] == i:
                x = i * i
                
                for j in range(x, N + 1, i):
                    if ref[j] == j:
                        ref[j] = i
                
            i += 1
        
        return 
        
        
    def findPrimeFactors(self, N):
        ref = [i for i in range(N + 1)]
        self.sieve(ref, N)
        
        # print(ref)
        
        prime_factors = []
        
        while N != 1:
            prime_factors.append(ref[N])
            
            N = N // ref[N]
                
        # print(prime_factors)
        return prime_factors

# -----------------------------------------------------------

# This will run for all test cases
'''
Constraints:

2<=N<=2*105
'''

class Solution:
    def __init__(self):
        self.INT_NUM = 10 ** 6 # Adjust this based on Constrains
        self.ref = [i for i in range(self.INT_NUM + 1)]
    
    def sieve(self):
        # Smallest Sieve
        i = 2
        
        while i * i <= self.INT_NUM:
            if self.ref[i] == i:
                x = i * i
                
                for j in range(x, self.INT_NUM+1, i):
                    if self.ref[j] == j:
                        self.ref[j] = i
                
            i += 1
        
        return 
        
        
    def findPrimeFactors(self, N):
        
        # print(self.ref)
        
        prime_factors = []
        
        while N != 1:
            prime_factors.append(self.ref[N])
            
            N = N // self.ref[N]
                
        # print(prime_factors)
        return prime_factors