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