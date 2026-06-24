# Tc: O(n) | Sc: O(n)

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        # Get the left side Max building height
        tallest_building = [0] * n
        left_max = height[0]
        for i in range(n):
            cur_building_height = height[i]

            left_max = max(left_max, cur_building_height)
            tallest_building[i] = left_max
        # print(tallest_building)

        # Get the right side Max building height
        right_max = height[n-1]
        for i in reversed(range(n)):
            cur_building_height = height[i]
            
            right_max = max(right_max, cur_building_height)
            tallest_building[i] = min(right_max, tallest_building[i])
        # print(tallest_building)

        # Calculate the rain water trapped
        trapped_water = 0
        for i in range(n):
            cur_building_height = height[i]
            trapped_water += (tallest_building[i] - cur_building_height)
        
        return trapped_water
