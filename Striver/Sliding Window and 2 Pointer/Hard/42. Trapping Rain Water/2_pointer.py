# Tc: O(n) | Sc: O(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left = 0
        right = n - 1

        left_tallest_building = -math.inf
        right_tallest_building = -math.inf

        trapped_water = 0

        while left < right:
            '''
                Select and Traverse the smallest buildings.
            '''

            left_building_height = height[left]
            right_building_height = height[right]

            if left_building_height <= right_building_height:
                '''
                    Right side building is tallest building
                '''
                if left_building_height >= left_tallest_building:
                    # If current building is the tallest amongst the Smallest buildings.
                    left_tallest_building = left_building_height
                else:
                    trapped_water += (left_tallest_building - left_building_height)
                
                left += 1
            else:
                '''
                    Left side building is tallest building
                '''
                if right_building_height >= right_tallest_building:
                    right_tallest_building = right_building_height
                else:
                    trapped_water += (right_tallest_building - right_building_height)
                
                right -= 1
        
        return trapped_water