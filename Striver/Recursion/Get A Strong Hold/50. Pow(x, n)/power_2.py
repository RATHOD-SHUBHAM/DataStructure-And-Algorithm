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