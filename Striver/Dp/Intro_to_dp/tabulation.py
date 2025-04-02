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
    print(obj.fib(697))  # Output: 802688355

# Time Complexity: O(n)
# Space Complexity: O(n).