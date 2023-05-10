class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # Helper Code ----------------------------------
        def exploreNeighbor_dfs(i , j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return -100000000 # return some random negative huge number -- assume to be negative infinity
            
            if grid[i][j] == 0:
                return 0
            
            # mark the current cell as visited
            grid[i][j] = 0
            
            
            count = 1 # current island size
            # check neighbor
            top_nei = exploreNeighbor_dfs(i-1 , j)
            bottom_nei = exploreNeighbor_dfs(i+1 , j)
            left_nei = exploreNeighbor_dfs(i , j+1)
            right_nei = exploreNeighbor_dfs(i , j-1)
            
            return count + (top_nei + bottom_nei + left_nei + right_nei)
        
        
        # Main Code ------------------------------------
        
        no_of_land = 0
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 0:
                    continue
                    
                count_of_land = exploreNeighbor_dfs(i , j)
                
                if count_of_land > 0:
                    no_of_land += count_of_land
        
        return no_of_land