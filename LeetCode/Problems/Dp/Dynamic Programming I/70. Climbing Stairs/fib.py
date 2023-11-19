class Solution:
    def climbStairs(self, n: int) -> int:
        fib = [1,1]
        
        for stair in range(2, n + 1): # include the nth number
            new_way = fib[0] + fib[1]
            fib[0] = fib[1]
            fib[1] = new_way
            
        return fib[1] if n > 0 else fib[0]