# Recursion for Fibonacci series

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
    
if __name__ == "__main__":
    n = 5
    obj = Solution()
    print(obj.fib(n))  # Output: 5

    print(obj.fib(0))  # Output: 0
    print(obj.fib(1))  # Output: 1
    print(obj.fib(2))  # Output: 1
    print(obj.fib(3))  # Output: 2
    print(obj.fib(4))  # Output: 3 
    print(obj.fib(697))  # Output: 802688355

# Time Complexity: O(2^n)
# Space Complexity: O(n) due to recursion stack.