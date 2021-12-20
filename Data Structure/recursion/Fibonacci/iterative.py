# Iterative
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        
        
        prev = 1
        othPrev = 0
        curSum = 0
        
        
        for _ in range(2,n+1):
            curSum = prev + othPrev
            othPrev = prev
            prev = curSum
            
        return curSum