# Time and Space = O(n) | O(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        
        # initialize pointers
        left = 0
        right = len(height) - 1
        
        leftMax = height[0]
        rightMax = height[-1]
        
        water_area = 0
        
        while left < right:
            
            # if my left boundary is smaller than right boundary
            if leftMax < rightMax:
                left += 1
                
                # calculate max of left boundary
                leftMax = max(leftMax, height[left])
                
                water_area += leftMax - height[left]
            
            else:
                right -= 1
                
                # calculate max of right boundary
                rightMax = max(rightMax , height[right])
                
                water_area += rightMax - height[right]
        
        return water_area