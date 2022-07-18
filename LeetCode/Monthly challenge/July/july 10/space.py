# https://www.youtube.com/watch?v=ktmzAZWkEZ0
# read the solution - Explanantion is fantastic

# Time = O(n)
# space = O(1)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one_step = two_step = 0
        
        for i in range(2 , len(cost)+1):
            temp = one_step
            
            one_step = min(one_step + cost[i-1] , two_step + cost[i-2])
            
            two_step = temp
            
        return one_step
            