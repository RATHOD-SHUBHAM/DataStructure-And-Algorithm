# ----------------------------------------------------------------

# 1. Extracting Last Digit

class Solution:
    def evenlyDivides (self, N):
        new_number = 0
        
        # Extract Last Digit
        while N > 0:
            remainder = N % 10
            new_number = new_number * 10 + remainder
            N = N // 10

        return new_number
    
# ----------------------------------------------------------------

# 2. HCF and LCM

class Solution:
    def GCD(self, a, b):
        if a == 0:
            return b
        return self.GCD(b%a, a)
    
    def LCM(self, a, b):
        return (a // self.GCD(a,b)) * b
        
    def lcmAndGcd(self, A , B):
        lcm = self.LCM(A,B)
        gcd = self.GCD(A, B)
    
        return [lcm,gcd]
    

# ----------------------------------------------------------------

# 3. Factors

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
    

# ----------------------------------------------------------------

# 4. Prime or Not

import math

class Solution:
    def check_prime(self, num):
        if num > 1 and num < 4:
            return True

        count = 0
        sqrt_n = math.floor(math.sqrt(num))

        for i in range(1, sqrt_n):
            if num % i == 0:
                count += 1

                if (num // i) != i:
                    count += 1

        
        if count == 2:
            return True
        else:
            return False



# ----------------------------------------------------------------

# 5. Sieve of Eratosthenes: All Primes Numbers between 1 to N

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        # Keep track of all the prime number
        ref = [True] * (n + 1)
        
        i = 2
        while (i * i) < n:
            if ref[i] == True:
                # mark all its mulitple as false - start from i * i
                for j in range(i*i, n + 1, i):
                    ref[j]=False
            
            i += 1
        
             
        primes = []
        for i in range(len(ref)):
            if i < 2:
                '''Prime number start from 2'''
                continue
            if ref[i] == True:
                primes.append(i)
        
        return primes
    
# ----------------------------------------------------------------

# 6. Pow(x, n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = self.power(x, abs(n))

        if n < 0:
            return 1 / result
        else:
            return result
    
    def power(self, x, n):
        if x == 0:
            return 0
        
        if n == 0:
            return 1
        
        if n % 2 == 0:
            result = self.power(x, n // 2)
            result = result * result
            return result
        else:
            result = self.power(x, n // 2)
            result = result * result
            result = x * result
            return result
        
# ----------------------------------------------------------------

# 7. Prime Factorization

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