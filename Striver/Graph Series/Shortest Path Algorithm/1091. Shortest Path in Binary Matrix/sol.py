# Dijstra algorithm

import heapq

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        minHeap = []
        heapq.heapify(minHeap)
        
        visited = set()
        
        src = (0,0)
        dest = (n-1, n-1)
        
        if grid[0][0] != 0:
            return -1
        
        heapq.heappush(minHeap, (1 , src))
        visited.add(src)

        
        # 8 directions
        neighbors = [(-1,-1), (-1,0), (-1, 1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        
        while minHeap:
            dist , node = heapq.heappop(minHeap)
            s_row , s_col = node
            
            if node == dest:
                return dist
            
            for neighbor in neighbors:
                adj_row , adj_col = neighbor
                
                nei_row = s_row + adj_row
                nei_col = s_col + adj_col
                
                if nei_row < 0 or nei_col < 0 or nei_row >= n or nei_col >= n or grid[nei_row][nei_col] == 1 or (nei_row, nei_col) in visited:
                    continue
                
                new_dist = 1 + dist
                
                heapq.heappush(minHeap, (new_dist , (nei_row, nei_col)))
                visited.add((nei_row, nei_col))
                
        return -1
        