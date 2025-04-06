import math
#User function Template for python3
class Solution:
    def minCost(self, height):
        n = len(height)
        
        # Base case
        if n < 2:
            return 0
            
        dp = [-1] * (n) # hold the minimum cost
        
        dp[0] = 0
        dp[1] = abs(height[0] - height[1])
        
        for i in range(2, n):
            cost_jump_1 = dp[i-1] + abs(height[i] - height[i-1])
            cost_jump_2 = dp[i-2] + abs(height[i] - height[i-2])
            
            dp[i] = min(cost_jump_1, cost_jump_2)
        
        return dp[n-1]
    
if __name__ == "__main__":
    height = [20, 30, 40, 20]
    obj = Solution()
    print(obj.minCost(height)) # Output: 20


    height = [10, 30, 40, 50, 20]
    obj = Solution()
    print(obj.minCost(height)) # Output: 50

    height = [10, 10, 10, 10]
    obj = Solution()
    print(obj.minCost(height)) # Output: 0
    
    height = [20, 30, 40, 30]
    obj = Solution()
    print(obj.minCost(height)) # Output: 10

    height = [319]
    obj = Solution()
    print(obj.minCost(height)) # Output: 0