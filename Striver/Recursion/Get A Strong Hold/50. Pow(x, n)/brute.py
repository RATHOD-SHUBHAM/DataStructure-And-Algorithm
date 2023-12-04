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
        