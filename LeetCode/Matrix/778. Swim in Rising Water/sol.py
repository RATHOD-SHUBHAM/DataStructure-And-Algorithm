class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        end_row = end_col = n
        
        # keep track of visited neighbors to prevent loop
        visited_nei = set()
        visited_nei.add((0,0)) # add the starting cell
        

        # keep selecting the cell with min value
        minHeap = [(grid[0][0] , 0 , 0)] # row and col
        
        while minHeap:
            curCell_val , curCell_row, curCell_col = heapq.heappop(minHeap)

            # check if we reached the end cell
            if curCell_row == end_row - 1 and curCell_col == end_col - 1:
                return curCell_val
            
            # traverse the path in 4 directions and check
            top = (curCell_row - 1, curCell_col)
            bottom = (curCell_row + 1, curCell_col)
            left = (curCell_row, curCell_col - 1)
            right = (curCell_row, curCell_col + 1)
            
            for row , col in (top, bottom, left, right):
                # check the bound
                if (row < 0 or row >= end_row) or (col < 0 or col >= end_col) or ((row, col) in visited_nei):
                    continue
                    
                # min_time_path = out of all the path , select the path that took min time to reach the end cell
                # change the wait time to waiting time in that path
                min_time_path = max(curCell_val , grid[row][col])

                
                heapq.heappush(minHeap , (min_time_path, row, col))
                visited_nei.add((row, col))
  