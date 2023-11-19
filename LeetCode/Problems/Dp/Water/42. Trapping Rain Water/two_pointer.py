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
                
            
                    
                