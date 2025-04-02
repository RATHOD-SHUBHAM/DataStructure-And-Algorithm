# Memoization - Top Down Approach

class Solution:
    def fib(self, n: int) -> int:
        dp  = [-1] * (n + 1)
        return self.fib_memo(n, dp)
    
    def fib_memo(self, n: int, dp: list) -> int:
        if dp[n] != -1:
            return dp[n]
        elif n <= 1:
            # Base case
            dp[n] = n
            return dp[n]
        else:
            # Recursive case
            dp[n] = self.fib_memo(n - 1, dp) + self.fib_memo(n - 2, dp)
            return dp[n]

    
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

# Time Complexity: O(n)
# Space Complexity: O(n).