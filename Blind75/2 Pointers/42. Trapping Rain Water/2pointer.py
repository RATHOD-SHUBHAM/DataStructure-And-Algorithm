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

            if height[left] < height[right]:
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