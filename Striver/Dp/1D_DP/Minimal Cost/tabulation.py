import math
#User function Template for python3
class Solution:
    def minimizeCost(self, k, arr):
        n = len(arr)
        dp = [-1] * (n)
        
        dp[0] = 0
        
        for idx in range(1, n):
            min_cost = math.inf
            for j in range(1, k+1):
                if idx - j < 0:
                    break
                
                cur_cost = dp[idx - j] + abs(arr[idx] - arr[idx - j])
                min_cost = min(cur_cost, min_cost)
            
            dp[idx] = min_cost
        
        return dp[n-1]

if __name__ == "__main__":
    # Example usage
    k = 3
    arr = [10, 30, 40, 50, 20]
    obj = Solution()
    print(obj.minimizeCost(k, arr))  # Output: 30