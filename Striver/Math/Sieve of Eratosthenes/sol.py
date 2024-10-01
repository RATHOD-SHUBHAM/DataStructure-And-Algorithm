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