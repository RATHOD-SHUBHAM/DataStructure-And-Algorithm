# Time and Space = O(n)

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0 
        
        leftHeight = height[:]
        rightHeight = height[:]
        
        # calculating max height on left side
        for i in range(1,len(height)):
            leftHeight[i] = max(height[i] , leftHeight[i-1])
        print(leftHeight)
        
        for i in reversed(range(len(height) - 1)):
            rightHeight[i] = max(height[i] , rightHeight[i+1])
        print(rightHeight)
        
        area_of_water = 0
        for i in range(len(height)):
            area_of_water += min(leftHeight[i] , rightHeight[i]) - height[i]
        print(area_of_water)
        
        return area_of_water