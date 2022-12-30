# Tc: O(n) andSc: O(1)

import math
class Solution:
    def maxArea(self, height: List[int]) -> int:
        container_with_most_water = -math.inf
        n = len(height)
        
        left = 0
        right= n - 1
        
        while left < right:
            container_height = min(height[left] , height[right])
            container_width = right - left
            
            container_area = container_height * container_width
            
            container_with_most_water = max(container_with_most_water , container_area)
            
            # try to increase contianer height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return container_with_most_water