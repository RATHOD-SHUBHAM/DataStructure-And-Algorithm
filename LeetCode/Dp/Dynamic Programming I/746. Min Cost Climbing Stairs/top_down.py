class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        n = len(cost)
        
        return self.dfs(n, memo, cost)
    
    
    def dfs(self, n , memo, cost):
        # base case
        if n in memo:
            return memo[n]
        
        # Minimum cost to reach step  0 or step 1 is 0
        # becasue we can directly jump 2 step
        if n < 2:
            return 0
        
        # cost to reach a step
        cost_1 = cost[n-1] + self.dfs(n - 1, memo, cost)
        cost_2 = cost[n-2] + self.dfs(n - 2, memo, cost)
        
        # cost to reach nth step is minimum cost of previous step
        memo[n] = min(cost_1 , cost_2)
        
        return memo[n]