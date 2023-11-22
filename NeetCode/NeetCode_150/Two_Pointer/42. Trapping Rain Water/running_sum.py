class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left_max_building = [0] * n
        right_max_building = [0] * n

        # Get the left side max building
        max_height = 0
        for i in range(n):
            cur_building = height[i]

            max_height = max(max_height , cur_building)

            left_max_building[i] = max_height
        
        print(left_max_building)

        # Get the right side max building height
        max_height = 0
        for i in reversed(range(n)):
            cur_building = height[i]

            max_height = max(max_height , cur_building)

            right_max_building[i] = max_height
        
        print(right_max_building)

        # Calculate the amount of water stored
        trapped_water = 0

        for i in range(n):
            cur_building = height[i]
            min_building = min(left_max_building[i], right_max_building[i])

            trapped_water += abs(cur_building - min_building)
        
        return trapped_water