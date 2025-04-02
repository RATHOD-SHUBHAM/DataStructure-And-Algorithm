# Space Optimized.

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        prev_1 = 0
        prev_2 = 1

        curr = 0

        for i in range(2, n+1):
            curr = prev_1 + prev_2 # fib(n) = fib(n-1) + fib(n-2)
            
            prev_1 = prev_2
            prev_2 = curr

        return curr

    
if __name__ == "__main__":
    n = 5
    obj = Solution()
    print(obj.fib(n))  # Output: 5

    print(obj.fib(0))  # Output: 0
    print(obj.fib(1))  # Output: 1
    print(obj.fib(2))  # Output: 1
    print(obj.fib(3))  # Output: 2
    print(obj.fib(4))  # Output: 3 

# Time Complexity: O(n)
# Space Complexity: O(1).