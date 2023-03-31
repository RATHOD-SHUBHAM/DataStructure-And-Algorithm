# Tc: O(n) | Sc: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0
        
        left = 0
        right = n - 1
        
        while left < right:
            width = right - left
            length = min(height[left] , height[right])
            
            area = length * width
            
            max_area = max(max_area, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area