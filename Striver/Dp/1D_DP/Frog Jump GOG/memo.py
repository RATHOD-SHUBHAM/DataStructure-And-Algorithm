import math
#User function Template for python3
class Solution:
    def minCost(self, height):
        n = len(height)
        dp = [-1] * (n)
        # 0 based index - hence n-1 will be the last index
        return self.memo(dp, n-1, height)
        
    
    def memo(self, dp, n, arr):
        if n == 0:
            # Cost it takes to jump from 0 to 0 step will be zero.
            return 0
        
        if dp[n] != -1:
            return dp[n]
        
        '''
        Cost it take to jump from 0 to n-1 index
        +
        Cost it takes to jump from n-1 to n index
        '''
        if n-1 >= 0:
            cost_jump_1 = self.memo(dp, n-1, arr) + abs(arr[n] - arr[n-1])
        else:
            cost_jump_1 = math.inf
        
        '''
        Cost it take to jump from 0 to n-2 index
        +
        Cost it takes to jump from n-2 to n index
        '''
        if n-2 >= 0:
            cost_jump_2 = self.memo(dp, n-2, arr) + abs(arr[n] - arr[n-2])
        else:
            cost_jump_2 = math.inf
        
        dp[n] = min(cost_jump_1, cost_jump_2)
        
        return dp[n]
    

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