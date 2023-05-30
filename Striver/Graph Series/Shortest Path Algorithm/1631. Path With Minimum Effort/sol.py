# Tc: O(VlogE) -> O((m*n)log(m*n))
# Sc: O(M * n)

import heapq
import math

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        
        distance = [[math.inf for _ in range(n)] for _ in range(m)]
        distance[0][0] = 0
        
        directions = [ (0,-1), (0,1), (-1, 0), (1, 0)]
        
        minHeap = []
        heapq.heapify(minHeap)
        heapq.heappush(minHeap, (0, (0,0)))
        
        
        while minHeap:
            effort , node = heapq.heappop(minHeap)
            row , col = node
            
            # if i reach the end cell. then i would have found the min distance
            if row == m - 1 and col == n - 1:
                return effort
            
            # parent effort
            parent_effort = heights[row][col]
            
            for direction in directions:
                nei_row , nei_col = direction
                
                # neighbors
                child_row = nei_row + row
                child_col = nei_col + col
                
                # edge
                if child_row < 0 or child_col < 0 or child_row >= m or child_col >= n:
                    continue
                
                child_effort = heights[child_row][child_col]
                
                # parent effort
                cur_effort = abs(parent_effort - child_effort)
                
                # get the max effort for the route
                max_effort = max(distance[row][col] , cur_effort)
                
                # condition check
                if max_effort < distance[child_row][child_col]:
                    distance[child_row][child_col] = max_effort
                    heapq.heappush(minHeap , (max_effort , (child_row , child_col) ) )             