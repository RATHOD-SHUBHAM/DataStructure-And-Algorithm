# TC : O(m * n) | Sc: O(min(m,n))
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        no_of_island = 0
        
        row_len = len(grid)
        col_len = len(grid[0])
        
        for row in range(row_len):
            for col in range(col_len):
                # check if the current cell is water
                if grid[row][col] == "0":
                    continue
                
                # this is land - check if this is surrounded by water
                queue = [(row,col)]
                
                # BFS
                while queue:
                    cur_row, cur_col = queue.pop(0)
                    
                    # Check if the node has been visited
                    if grid[cur_row][cur_col] == "0":
                        continue
                    
                    grid[cur_row][cur_col] = "0" # mark the current node as visited
                    
                    # Explore its adjacent neighbor
                    adj_nei = self.getAdjacentNeighbor(cur_row, cur_col, grid)
                    
                    for nei in adj_nei:
                        nei_row, nei_col = nei
                        
                        # if the neigbor is a land - attach it to island
                        if grid[nei_row][nei_col] == "1":
                            queue.append((nei_row, nei_col))
                             
                # island has been explore - increase the count before moving to the next one
                no_of_island += 1
        
        return no_of_island
    
    def getAdjacentNeighbor(self, row, col, matrix):
        adjNeighbor = []

        # up
        if row > 0:
            adjNeighbor.append([row - 1 , col])
        # down
        if row < len(matrix) - 1:
            adjNeighbor.append([row + 1 , col])

        # left
        if col > 0:
            adjNeighbor.append([row , col - 1])
        # right
        if col < len(matrix[0]) - 1:
            adjNeighbor.append([row , col + 1])

        return adjNeighbor
            