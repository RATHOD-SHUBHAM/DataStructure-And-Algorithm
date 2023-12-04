# TLE

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        result = 1
        mod = (10 ** 9) + 7

        for i in range(n): 
            if i % 2 == 0:
                result *= 5
            elif i % 2 == 1:
                result *= 4
        
        return (result % mod)
    

# -------------------------------------------------------

# Memory Error

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = (10 ** 9) + 7

        # get the odd place and even place
        no_of_odd_places = n // 2
        no_of_even_place = (n // 2) + (n % 2)

        # Compute Place holder value
        odd_res = self.power(4 , no_of_odd_places) 
        even_res = self.power(5 , no_of_even_place)

        return (odd_res * even_res) % MOD

    
    def power(self, x, n):
        if x == 0:
            return 0
        
        if n == 0:
            return 1
        
        if n % 2 == 0:
            result = self.power(x , n // 2)
            result = result * result
            
            return result
        
        elif n % 2 == 1:
            result = self.power(x , n // 2)
            result = result * result

            result = x * result
            return result
        
# -------------------------------------------------------

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = (10 ** 9) + 7

        # get the odd place and even place
        no_of_odd_places = n // 2
        no_of_even_place = (n // 2) + (n % 2)

        # Compute Place holder value
        '''Pass mod as the result should be in range (10 ^ 9 + 7)'''
        odd_res = self.power(4 , no_of_odd_places, MOD) 
        even_res = self.power(5 , no_of_even_place, MOD)

        return (odd_res * even_res) % MOD

    
    def power(self, x, n, MOD):
        if x == 0:
            return 0
        
        if n == 0:
            return 1
        
        if n % 2 == 0:
            result = self.power(x , n // 2, MOD)
            result = result * result
            
            return result % MOD
        
        elif n % 2 == 1:
            result = self.power(x , n // 2, MOD)
            result = result * result

            result = x * result
            return result % MOD