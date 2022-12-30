# Tc and Sc: O(n) 
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        # store the left and right max value
        left_max = [-math.inf] * n 
        right_max = [-math.inf] * n 
        
        
        # get the left max building
        max_val = -math.inf
        for i in range(n):
            cur_val = height[i]
            
            if cur_val > max_val:
                max_val = cur_val
                left_max[i] = max_val
            else:
                left_max[i] = max_val
                
        print(left_max)
        
        # get the right max building
        max_val = -math.inf
        for i in reversed(range(n)):
            cur_val = height[i]
            
            if cur_val > max_val:
                max_val = cur_val
                right_max[i] = max_val
            else:
                right_max[i] = max_val
                
        print(right_max)
                
        # calculate volume of water at each block
        total_volume = 0
        for i in range(n):
            cur_block_height = height[i]
            
            volume_of_water_at_the_block = min(left_max[i] , right_max[i]) - cur_block_height
            
            total_volume += volume_of_water_at_the_block
        
        print(total_volume)
        
        return total_volume