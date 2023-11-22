# Running Sum --------------------------------------------------------------------------------

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


# Two Pointer --------------------------------------------------------------------------------

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left = 0
        right = n - 1

        left_max_building = -math.inf
        right_max_building = -math.inf

        trapped_water = 0

        while left < right:
            # check which building is smaller
            if height[left] <= height[right]:
                # Check if this is the left most taller building
                if height[left] >= left_max_building:
                    left_max_building = height[left]

                else:
                    # on the left side there is a taller building than the current building
                    trapped_water +=  left_max_building - height[left]
                    # here we know that left building is smaller than right building only then we enter this loop
                
                left += 1
                

            else:
                # if right building is smaller than left building
                if height[right] >= right_max_building:
                    right_max_building = height[right]
                
                else:
                    # on the right side there is a taller building than the current building
                    trapped_water +=  right_max_building - height[right]
                    # here we know that right building is smaller than left building only then we enter this loop

                right -= 1

        
        return trapped_water