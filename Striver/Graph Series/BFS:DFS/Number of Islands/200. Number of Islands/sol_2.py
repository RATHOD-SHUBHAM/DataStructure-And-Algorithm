class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        no_of_island = 0

        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        visited = [[False for _ in range(n)] for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "0" or visited[row][col] == True:
                    continue

                self.dfs(row, col, visited, neighbors, m , n, grid)

                no_of_island += 1

        return no_of_island
    
    def dfs(self, row, col, visited, neighbors, m , n, grid):
        if row < 0 or col < 0 or row >= m or col >= n or visited[row][col] == True or grid[row][col] == "0":
            return
        
        visited[row][col] = True

        for neighbor in neighbors:
            adj_row, adj_col = neighbor

            nei_row = row + adj_row
            nei_col = col + adj_col

            self.dfs(nei_row, nei_col, visited, neighbors, m , n, grid)
        
        return
