class Solution:
    def fib(self, n: int, memo = {0:0, 1:1}) -> int:
        if n in memo:
            return memo[n]
        
        
        memo[n] = self.fib(n - 1 , memo) + self.fib(n - 2, memo)
        
        return memo[n]