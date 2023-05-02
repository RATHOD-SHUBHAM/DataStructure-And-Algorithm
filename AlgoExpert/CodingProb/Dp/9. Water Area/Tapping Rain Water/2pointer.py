# two pointer
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        left = 0
        right = n - 1
        
        left_max = -math.inf
        right_max = -math.inf
        
        trapped_water = 0
        
        while left < right:
            if height[left] <= height[right]:
                if left_max <= height[left]:
                    left_max = height[left]
                else:
                    trapped_water += left_max - height[left]
                
                left += 1
            
            else:
                if right_max <= height[right]:
                    right_max = height[right]
                else:
                    trapped_water += right_max - height[right]
                
                right -= 1
                
        return trapped_water