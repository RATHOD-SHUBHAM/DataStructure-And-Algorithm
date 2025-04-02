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

# Time Complexity: O(2^n)
# Space Complexity: O(n) due to recursion stack.

# ---------------------------------- Memoization - Top Down Approach ----------------------------------
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

# Time Complexity: O(n).
# Space Complexity: O(n) due to recursion stack.


# ---------------------------------- Tabulation - Bottom Up Approach ----------------------------------
# Tabulation - Bottom Up Approach

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        
        dp = [0] * (n + 1)

        # Base case
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]

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

# Time Complexity: O(n)
# Space Complexity: O(n).

# ---------------------------------- Space Optimized ----------------------------------
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