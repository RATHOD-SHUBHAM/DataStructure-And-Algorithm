class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        visited = [[False for _ in range(n)] for _ in range(m)]
        distinctIsland = set()
        
        for i in range(m):
            for j in range(n):
                
                cur_island_list = []
                
                # if island and not visited
                if grid[i][j] == 1 and visited[i][j] == False:
                    # start point
                    row_origin = i
                    col_origin = j
                    
                    self.dfs(i, j , row_origin, col_origin, cur_island_list, visited, grid, m , n)
                    
                    # print(cur_island_list)

                    distinctIsland.add(tuple(cur_island_list))
                    # print(distinctIsland)
                    
        # print(distinctIsland)
        return len(distinctIsland)
    
    
    def dfs(self, i, j , row_origin, col_origin, cur_island_list, visited, grid, m, n):
        # base case
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or visited[i][j] == True:
            return 
        
        # mark visited
        visited[i][j] = True
        
        # get the coordinates
        row_coord = i - row_origin
        col_coord = j - col_origin
        
        coordinates = (row_coord, col_coord)
        
        cur_island_list.append(coordinates)
        
        # traverse in 4 direction
        self.dfs(i + 1, j , row_origin, col_origin, cur_island_list, visited, grid, m , n)
        self.dfs(i - 1, j , row_origin, col_origin, cur_island_list, visited, grid, m , n)
        self.dfs(i, j + 1 , row_origin, col_origin, cur_island_list, visited, grid, m , n)
        self.dfs(i, j - 1, row_origin, col_origin, cur_island_list, visited, grid, m , n)     