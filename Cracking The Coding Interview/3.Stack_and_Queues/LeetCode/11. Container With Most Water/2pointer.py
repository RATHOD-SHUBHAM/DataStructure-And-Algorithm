class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        maxArea = -inf
        
        while left < right:
            curHeight = min(height[left], height[right])
            curWidth = right - left
            curArea = curHeight * curWidth
            
            maxArea = max(maxArea, curArea)
            
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
                
        return maxArea