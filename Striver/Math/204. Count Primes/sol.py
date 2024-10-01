class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        # Keep track of all the prime number
        ref = [True] * (n) # n and not n + 1 becasue m we track number that are strictly less than n
        
        i = 2
        while (i * i) < n:
            if ref[i] == True:
                # mark all its mulitple as false - start from i * i
                for j in range(i*i, n, i):
                    ref[j]=False
            
            i += 1
        
        return ref.count(True) - 2 # -2 because of starting idx -> 0 and 1