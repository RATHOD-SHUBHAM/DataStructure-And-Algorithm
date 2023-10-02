# Running Sum

# Tc and Sc: O(n) 
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        # store the left and right max value
        left_max = [-math.inf] * n 
        right_max = [-math.inf] * n 
        
        
        # get the left max building
        curMax = -math.inf
        for i in range(n):
            curHeight = height[i]
            curMax = max(curHeight, curMax)
            left_max[i] = curMax
                
        print(left_max)
        
        # get the right max building
        curMax = -math.inf
        for i in reversed(range(n)):
            curHeight = height[i]
            curMax = max(curHeight, curMax)
            right_max[i] = curMax
                
        print(right_max)
                
        # calculate volume of water at each block
        trapped_water = 0
        for i in range(n):
            trapped_water += min(left_max[i], right_max[i]) - height[i]
        
        print(trapped_water)
        
        return trapped_water
    