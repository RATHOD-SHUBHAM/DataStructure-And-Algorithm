'''
if n is negative. In that case, the answer will be the reciprocal of the result if n were positive.
(x ^ n) = (1/x ^ −n) where n<0.
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 1:
            return 1/ self.myPow(x, -n)

        return x * self.myPow(x, n -1)
    
# ---------------------------------------------------------------------------------------------------
    

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
        
        return x * self.power(x , n - 1)
        
# ---------------------------------------------------------------------------------------------------

'''
Binary exponentiation
# 3 Rules:

    1. If n is negative. 
    In that case, the answer will be the reciprocal of the result if n were positive.
        (x ^ -n) = (1/x ^ n) where n<0.

    2. If n is even:
        (x ^ n) = (x ^ n/2) * (x ^ n/2)

    3. If n is odd:
        (x ^ n) = x * (x ^ n - 1 ), where
            (x ^ n - 1)  = lets assume it to be (x ^ m) , where m is even
                so, (x ^ m) = (x ^ m /2) * (x ^ m /2)
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle -ve `n` value
        result = self.power(x, abs(n))

        if n < 0:
            return 1 / result
        else:
            return result
        
    def power(self, x, n):
        if x == 0:
            return 0
        
        if n == 0:
            return 1 # anything to power 0 = 1
        
        # If `n` is even
        if n % 2 == 0:
            # [x^n] = [(x^n/2) * (x^n/2)]
            result = self.power(x , n // 2)
            result = result * result
            return result
        else:
            # `n` is odd 
            # [x^n] = [x * (x^m/2) * (x^m/2)]
            result = self.power(x , n // 2)
            result = result * result # [x ^ m]
            
            result = x * result # x * [x ^ m]
            return result
        
# ---------------------------------------------------------------------------------------------------
        
'''
# 3 Rules:

    1. If n is negative. 
    In that case, the answer will be the reciprocal of the result if n were positive.
        (x ^ -n) = (1/x ^ n) where n<0.

    2. If n is even
        (x ^ n)= (x ^ n//2 )* (x ^ n//2)

    3. If n is odd
        (x ^ n) = x * (x ^ n - 1//2) * (x ^ n - 1//2)
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = self.power(x, abs(n))

        if n < 0:
            return 1 / result
        else:
            return result
        
    
    def power(self, x, n):
        if n == 0:
            return 1
        
        if x == 0:
            return 0
        
        if n % 2 == 0:
            result = self.power(x * x, n // 2)
            return result
        else:
            result = self.power(x * x , (n - 1)// 2)
            result = x * result
            return result