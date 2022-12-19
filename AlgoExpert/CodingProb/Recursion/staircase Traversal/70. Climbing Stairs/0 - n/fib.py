class Solution:
    def climbStairs(self, n: int) -> int:
        fib = [1, 1]
        
        for i in range(2, n + 1):
            new_stair = fib[0] + fib[1]
            fib[0] = fib[1]
            fib[1] = new_stair
        
        return fib[1] if n > 0 else fib[0]