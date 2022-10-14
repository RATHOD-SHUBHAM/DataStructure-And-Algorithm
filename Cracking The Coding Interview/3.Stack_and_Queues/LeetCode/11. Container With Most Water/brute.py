# brute force
# Tc: O(n^2)
# Sc: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        maxArea = -inf
        
        for i in range(n):
            for j in range(i+1 , n):
                curHeight = min(height[i] , height[j])
                curWidth = j - i
                curArea = curHeight * curWidth
                
                maxArea = max(maxArea , curArea)
        
        return maxArea
