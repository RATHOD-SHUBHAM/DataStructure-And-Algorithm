'''
Cannonical representation of a point:

- To Find 4 possible Reflections for this shape.
For each point (x, y) in the original shape, it has 4 corresponding reflection points.
• (x, y) → (1,1)
• (-x, y) → (-1,1)
• (x, -y) → (1,-1)
• (-x, -y) → (-1,-1)
Find all these, sort them, and add them to our list of reflections.

-To Find 4 possible Rotations for this shape.
For each point (x, y) in the original shape, it has 4 corresponding rotated points.
• (y, x) → (1,1)
• (y, -x) → (1,-1)
• (-y, x) → (-1,1)
• (-y, -x) → (-1,-1)
Find all these, sort them and add to our list of rotations.
'''

class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        directions = [(-1, 0), (1,0), (0,-1),(0,1)]

        # cannonical representation of a point
        cannonical_rep = [(1,1), (-1,1), (1,-1), (-1,-1)]

        distinct_island = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # capture all the neighbouring island
                    coordinates = []
                    self.neighbor_island(i, j, coordinates, directions, m ,n ,grid) # DFS

                    # capture cannocical form
                    cannonical_coordinates = self.cannonical(coordinates, cannonical_rep)
                    distinct_island.add(tuple(cannonical_coordinates))
            
        return len(distinct_island)
    
    def neighbor_island(self, row, col, coordinates, directions, m ,n ,grid):
        if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0:
            return
        
        # mark the current cell as visited by changing to 0
        grid[row][col] = 0

        coordinates.append((row, col))

        for adj_row, adj_col in directions:
            nei_row = row + adj_row
            nei_col = col + adj_col

            self.neighbor_island(nei_row, nei_col, coordinates, directions, m ,n ,grid)
        
        return 
    

    def cannonical(self, coordinates, cannonical_rep):
        shapes = []

        for i , j in cannonical_rep:
            # Reflections
            shape = []
            for x, y in coordinates:
                x = x * i
                y = y * j

                shape.append((x,y))
                # print("before: ", shape)
                shape = sorted(shape)
                # print("after: ", shape)
            # print(shape)

            _shape = []
            for x, y in shape:
                x = x - shape[0][0] # Row origin
                y = y - shape[0][1] # col origin

                _shape.append((x, y))
            # print("reflection_shape: ", _shape)


            shapes.append(_shape)
            # print("reflection Shapes: ", shapes)

            # Rotation
            shape = []
            for x, y in coordinates:
                y = y * i
                x = x * j

                shape.append((y,x))
                shape = sorted(shape)
            # print(shape)

            _shape = []
            for x, y in shape:
                x = x - shape[0][0] # Row origin
                y = y - shape[0][1] # Col origin

                _shape.append((x, y))
            # print("rotation_shape: ", _shape)

            shapes.append(_shape)
        #     print("rotation Shapes: ", shapes)
        
        print("shapes",shapes)
        print("min shapes",min(shapes))

        print("\n")

        return min(shapes)