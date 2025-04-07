import math
#User function Template for python3
class Solution:
    def minimizeCost(self, k, arr):
        n = len(arr)
        dp = [-1] * (n)
        
        return self.memo(dp, n-1, k, arr)
    
    def memo(self, dp, n, k, arr):
        if n == 0:
            return 0
        
        if dp[n] != -1:
            return dp[n]
        
        min_cost = math.inf
        for i in range(1, k+1):
            if n - i < 0:
                break
            cur_cost = self.memo(dp, n-i, k, arr) + abs(arr[n] - arr[n-i])
            min_cost = min(cur_cost, min_cost)
        
        dp[n] = min_cost
        return dp[n]

if __name__ == "__main__":
    # Example usage
    k = 3
    arr = [10, 30, 40, 50, 20]
    obj = Solution()
    print(obj.minimizeCost(k, arr))  # Output: 30