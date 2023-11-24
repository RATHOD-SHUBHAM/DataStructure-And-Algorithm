class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        # DFS -----
        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or visited[row][col] == True or grid[row][col] == "0":
                return
            
            visited[row][col] = True

            for adj_row, adj_col in directions:
                nei_row = adj_row + row
                nei_col = adj_col + col

                dfs(nei_row, nei_col)

            return

        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0" or visited[i][j] == True:
                    continue
                
                dfs(i,j)
                count += 1
        
        return count