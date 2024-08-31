# -------------------  Prefix Sum  -------------------

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


# -------------------  One Prefix Sum  -------------------

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


# -------------------  2 Pointers  -------------------


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