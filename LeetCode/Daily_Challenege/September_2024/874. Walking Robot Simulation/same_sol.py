class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Store obstacles in an set for efficient lookup
        obstacle_set = set()
        for obs in obstacles:
            obstacle_set.add(tuple(obs))

        # Define direction vectors: North, East, South, West
        # 0: North, 1: East, 2: South, 3: West
        directions = [(0, 1), (1, 0), (0, -1),  (-1, 0)]
        
        current_direction = 0  
        x, y = 0, 0
        max_distance_squared = 0
        
        for command in commands:
            if command == -1:  # Turn right
                current_direction = (current_direction + 1) % 4
            
            elif command == -2:  # Turn left
                current_direction = (current_direction - 1) % 4
                # current_direction = (current_direction + 3) % 4
            else:
                # Move forward
                dx, dy = directions[current_direction]

                # Move Step by Step
                for _ in range(command):
                    next_x, next_y = x + dx, y + dy
                    
                    if (next_x, next_y) in obstacle_set:
                        break
                    
                    x, y = next_x, next_y

                squared_euclidean_dist = (x * x) + (y * y)
                max_distance_squared = max(max_distance_squared, squared_euclidean_dist)

        return max_distance_squared