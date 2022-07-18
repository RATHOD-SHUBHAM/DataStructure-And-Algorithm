# https://www.youtube.com/watch?v=ktmzAZWkEZ0
# read the solution - Explanantion is fantastic

# Time = O(n)
# space = O(n)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        
        def mincost(i):
            if i <= 1:
                return 0
            
            if i in memo:
                return memo[i]
            
            one_step = cost[i-1] + mincost(i-1)
            two_step = cost[i-2] + mincost(i-2)
            memo[i] = min(one_step , two_step)
            
            return memo[i]
            
        return mincost(len(cost))
            