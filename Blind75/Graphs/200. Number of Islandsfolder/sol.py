class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        visited = [[False for _ in range(m)] for _ in range(n)]

        directions = [(0,1),(1,0),(0,-1), (-1, 0)]

        no_of_island = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and visited[i][j] == False:
                    visited[i][j] = True

                    # Explore Neighbor
                    self.explore(i, j, n, m, grid, visited, directions)

                    no_of_island += 1

        return no_of_island

    def explore(self, i, j, n, m, grid, visited, directions):
        for r, c in directions:
            nei_r = i + r
            nei_c = j + c

            if nei_r < 0 or nei_r >= n or nei_c < 0 or nei_c >= m or visited[nei_r][nei_c] == True or grid[nei_r][nei_c] == "0":
                continue
            
            visited[nei_r][nei_c] = True

            # Explore Neighbor
            self.explore(nei_r, nei_c, n, m, grid, visited, directions)
        
        return