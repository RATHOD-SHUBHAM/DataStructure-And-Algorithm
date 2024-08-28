# Tc: O(n) | Sc: O(2n)

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        # Get the left side Max building height
        left_side_tallest_building = [0] * n
        left_max = height[0]
        for i in range(n):
            cur_building_height = height[i]

            left_max = max(left_max, cur_building_height)
            left_side_tallest_building[i] = left_max
        # print(left_side_tallest_building)

        # Get the right side Max building height
        right_side_tallest_building = [0] * n
        right_max = height[n-1]
        for i in reversed(range(n)):
            cur_building_height = height[i]
            
            right_max = max(right_max, cur_building_height)
            right_side_tallest_building[i] = right_max
        # print(right_side_tallest_building)

        # Calculate the rain water trapped
        trapped_water = 0
        for i in range(n):
            min_building_height = min(left_side_tallest_building[i], right_side_tallest_building[i])
            cur_building_height = height[i]

            trapped_water += (min_building_height - cur_building_height)
        
        return trapped_water
