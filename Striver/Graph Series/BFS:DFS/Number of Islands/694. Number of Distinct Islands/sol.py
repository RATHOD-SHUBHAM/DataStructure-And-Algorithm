'''
    Main idea is the get the cell coordinates

    row_coordinate = i - row_origin
    col_coordinate = j - col_origin

    # Note: abs difference will give an error
'''
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]

        directions = [(-1,0), (1,0), (0,-1), (0,1)] 

        no_of_islands = set()

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 0 or visited[i][j] == True:
                    continue

                row_origin = i
                col_origin = j

                current_island = []

                self.dfs(i , j, row_origin, col_origin, current_island, visited, directions, grid, m, n)

                no_of_islands.add(tuple(current_island))
        
        return len(no_of_islands)


        
    def dfs(self, i , j, row_origin, col_origin, current_island, visited, directions, grid, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0 or visited[i][j] == True:
            return
        
        visited[i][j] = True

        row_coordinate = i - row_origin
        col_coordinate = j - col_origin

        current_island.append((row_coordinate, col_coordinate))

        for adj_row ,adj_col in directions:
            nei_row = adj_row + i
            nei_col = adj_col + j

            self.dfs(nei_row , nei_col, row_origin, col_origin, current_island, visited, directions, grid, m, n)

        return