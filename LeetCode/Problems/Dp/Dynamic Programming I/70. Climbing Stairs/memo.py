# recursion
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0:1}
        
        return self.dfs(n , memo)
    
    def dfs(self, n , memo):
        # base case
        if n in memo:
            return memo[n]
        
        if n < 0:
            return 0
        
        no_of_ways = 0
        for step in range(1,3):
            cur_height = n - step
            no_of_ways += self.dfs(cur_height , memo)
        memo[n] = no_of_ways
            
        return memo[n]
            
        