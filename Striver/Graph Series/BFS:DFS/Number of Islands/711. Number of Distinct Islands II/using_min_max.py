"""
Grid traversal: O(m × n)
All DFS calls: O(m × n)
All canonical generations: O(k₁ log k₁ + k₂ log k₂ + ... + kᵢ log kᵢ) = 8 * O(k log k) 

so Tc= O(m × n log(m × n))

Space
coords = O(K)
recursion stack = O(m × n)

Total: O(m × n)
"""

class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        directions = [(0,-1), (0,1), (1,0), (-1,0)]

        # Sign-flip pairs. With and without swapping x/y (done below),
        # these cover all 8 symmetries: 4 rotations × 2 reflections.
        # (i, j) multiplies row by i and col by j to flip across axes.
        canonical_directions = [(1,1),(1,-1),(-1,1),(-1,-1)]

        distinct_island = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                # get island corrdinates
                coords = []
                self.dfs(i,j, coords, directions, m ,n, grid)

                cannocial_coords = self.cannonical_point(coords, canonical_directions)

                # If min is used
                distinct_island.add(tuple(sorted(cannocial_coords)))

                # If sorting is used
                # canonical_coords_as_tuples = [tuple(coord) for coord in cannocial_coords]
                # distinct_island.add(tuple(sorted(canonical_coords_as_tuples)))
        
        return len(distinct_island)

    def dfs(self, i, j, coords, directions, m ,n, grid):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0 :
            return
        
        grid[i][j] = 0

        coords.append((i,j))

        for adj_row, adj_col in directions:
            nei_row = i + adj_row
            nei_col = j + adj_col

            self.dfs( nei_row , nei_col, coords, directions, m ,n, grid)
        
        return 
    
    def cannonical_point(self, coords, canonical_directions):
        """
        Build all 8 transformed versions of the island:
          - 4 sign-flip variants without swapping (reflections across axes)
          - 4 variants with x/y swapped (90° rotation effect) + sign flips
        For each variant:
          1) Sort points to get a stable order
          2) Translate so the smallest point becomes (0,0) (remove translation)
        Return the lexicographically smallest normalized variant as the signature.
        """
        shapes = [] # Contains 8 transformed versions

        for i , j in canonical_directions:

            # ---------- Variant A: Flipping with no swap (x, y) -> (i*x, j*y) ----------
            shape = []
            for x , y in coords:
                x = x * i
                y = y * j

                shape.append((x,y))
            
            # Normalize
            shape = sorted(shape) # Sorting
            
            _shape = [] # Transforming
            for x , y in shape:
                x = x - shape[0][0]
                y = y - shape[0][1]

                _shape.append((x, y))
            
            shapes.append(_shape) # 4 sign-flip variants without swapping

            # ---------- Variant B: swap (x, y) -> (j*y, i*x) ----------
            # Swap acts like a 90° rotation; with sign flips, covers remaining symmetries
            shape = []
            for x , y in coords:
                y = y * i
                x = x * j

                shape.append((y,x))

            # Normalize
            shape = sorted(shape) # Sorting
            
            _shape = [] # Transforming
            for x , y in shape:
                x = x - shape[0][0]
                y = y - shape[0][1]

                _shape.append((x,y))
            
            shapes.append(_shape) # 4 sign-flip variants with swapping

        # print(shapes) # total 8 variants
        return min(shapes)
    

# ---------------------- Using Max ------------------------
class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        distinct_island = set()

        neighbors = [[0,1], [0,-1], [1,0], [-1,0]]

        canonical_directions = [[1,1], [1,-1], [-1,1], [-1,-1]]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                
                coords = []
                self.dfs(i, j, coords, neighbors, grid, m ,n)
                print(coords)

                canonical_coords = self.canonical_points(coords, canonical_directions)

                distinct_island.add(tuple(canonical_coords))
            
        # print(distinct_island)

        return len(distinct_island)



        
    def dfs(self, i, j, coords, neighbors, grid, m ,n):
        # base case
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
            return
        
        grid[i][j] = 0

        coords.append((i,j))

        for nei in neighbors:
            nei_i = i + nei[0]
            nei_j = j + nei[1]

            self.dfs(nei_i, nei_j, coords, neighbors, grid, m ,n)
        
        return
    
    def canonical_points(self, coords, canonical_directions):
        shapes = []

        for i, j in canonical_directions:
            # No flip
            shape = []

            for x, y in coords:
                x = i * x
                y = j * y

                shape.append((x,y))
            
            # Normalize
            shape.sort()
            # print("ref_shape: ",shape)
            _shape = []
            for x, y in shape:
                x = x - shape[0][0]
                y = y - shape[0][1]

                _shape.append((x,y))
            _shape.sort()

            shapes.append(_shape)

            # Flip
            shape = []
            for x, y in coords:
                y = i * y
                x = j * x

                shape.append((y,x))
            
            # Normalize
            shape.sort()
            # print("rot_shape: ",shape)
            _shape = []
            for x, y in shape:
                x = x - shape[0][0]
                y = y - shape[0][1]

                _shape.append((x,y))
            _shape.sort()

            shapes.append(_shape)
        
        # print(shapes)
        # print("------")
        return max(shapes)
