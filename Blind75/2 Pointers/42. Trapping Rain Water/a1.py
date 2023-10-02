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
    
# ------------------------------------------------------------------------

# Two Pointer

# Water will be stored upto the max height of the min building
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        left = 0
        right = n - 1
        
        left_max = -math.inf
        right_max = -math.inf
        
        total_volume = 0
        while left < right:
            # chose the building with small height: this gurantees that on the right side there is a building which is greater than or equal to current building size
            if height[left] <= height[right]:
                # if my current building is taller than left max building
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    # water can be store here
                    total_volume += left_max - height[left]
                
                left += 1
            
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    # water can be store here
                    total_volume += right_max - height[right]
                
                right -= 1
                
        return total_volume
    

# ------------------------------------------------------------------------


# Easier 2 pointer:

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left = 0
        right = n - 1

        leftMax = -math.inf
        rightMax = -math.inf

        trapped_water = 0

        '''
            So, we can say that if there is a larger bar at one end (say right), 
            we are assured that the water trapped would be dependant on height of bar in 
            current direction (from left to right). 
        '''

        while left < right:

            if height[left] <= height[right]:
                if height[left] >= leftMax:
                    # if the building height is same as or more than taller building than water cant be stored
                    leftMax = height[left]
                else:
                    # Checking if right side building is taller than tallest left side
                    if height[right] >= leftMax:
                        trapped_water += leftMax - height[left]
                
                left += 1
            
            else:
                if height[right] >= rightMax:
                    # Checking taller building
                    rightMax = height[right]
                else :
                    # Checking if left side building is taller than tallest right side
                    if height[left] >= rightMax:
                        trapped_water += rightMax - height[right]
                right -= 1

            
            
        return trapped_water
        

    
    