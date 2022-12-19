class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        idx = 0
        return self.dfs(idx , n , memo)
    
    def dfs(self, idx, n , memo):
        if idx > n:
            return 0
        
        if idx == n:
            return 1
        
        if idx in memo:
            return memo[idx]
        
        memo[idx] = self.dfs(idx + 1 , n , memo) + self.dfs(idx + 2 , n , memo)
        
        return memo[idx]
        