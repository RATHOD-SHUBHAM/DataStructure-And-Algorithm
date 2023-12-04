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