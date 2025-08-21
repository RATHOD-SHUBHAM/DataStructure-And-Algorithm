class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False for _ in range(n)] for _ in range(m)]

        # Store the normalized coordinates
        no_of_distinct_island = set()

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0 or visited[row][col] == True:
                    continue
                
                current_island_coordinates = []

                origin_row = row
                origin_col = col

                self.dfs(row, col, origin_row, origin_col, current_island_coordinates, visited, grid, m, n)

                print(tuple(current_island_coordinates))

                no_of_distinct_island.add(tuple(current_island_coordinates))
            
        return len(no_of_distinct_island)


    def dfs(self, row, col, origin_row, origin_col, current_island_coordinates, visited, grid, m, n):
        # check for boundaries
        if row < 0 or col < 0 or row >= m or col >= n or grid[row][col] == 0 or visited[row][col] == True:
            return
        
        # mark the cell as visited
        visited[row][col] = True

        # Coordinate Normalization
        row_no = row - origin_row
        col_no = col - origin_col

        # Append as tuple
        current_island_coordinates.append((row_no, col_no))

        # Explore Neighbors
        neighbors = [[0,-1], [0,1], [-1,0], [1,0]]
        for nei in neighbors:
            nei_row = nei[0] + row
            nei_col = nei[1] + col

            self.dfs(nei_row, nei_col, origin_row, origin_col, current_island_coordinates, visited, grid, m, n)
        
        return current_island_coordinates