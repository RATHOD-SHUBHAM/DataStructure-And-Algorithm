# https://www.youtube.com/watch?v=ktmzAZWkEZ0
# read the solution - Explanantion is fantastic

# Time = O(n)
# space = O(n)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # len + 1 because we will have to go outside the cost to reach the top
        min_cost = [0] * (len(cost) + 1)
        
        
        for i in range(2 , len(cost) + 1):
            one_step = cost[i-1] + min_cost[i-1]
            two_step = cost[i-2] + min_cost[i-2]
            min_cost[i] = min(one_step , two_step)
            print(min_cost)
            
        return min_cost[-1]
            