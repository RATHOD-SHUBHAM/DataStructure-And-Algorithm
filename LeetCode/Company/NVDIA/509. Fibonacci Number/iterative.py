class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        cache = [0] * (n + 1)
        cache[1] = 1

        for i in range(2, n + 1):
            cache[i] = cache[i-1] + cache[i-2]
        
        return cache[n]