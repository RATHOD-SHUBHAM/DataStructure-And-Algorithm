# Tc adn Sc: O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # keep track of the cost to reach a given step
        dp = [0] * (n + 1)
        
        # start from step 2
        for step in range(2, n+1):
            cost_1 = cost[step - 1] + dp[step - 1]
            cost_2 = cost[step - 2] + dp[step - 2]
            dp[step] = min(cost_1 , cost_2)
            
        return dp[-1]
            