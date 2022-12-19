class Solution:
    def climbStairs(self, n: int) -> int:
        # start from 0 and check how many possible ways are there to reach n
        idx = 0
        return self.dfs(idx , n)
    
    def dfs(self, idx , n):
        # base case
        if idx > n:
            return 0
        
        if idx == n:
            return 1
        
        # explore the steps
        return self.dfs(idx + 1, n) + self.dfs(idx + 2, n)
        