'''
Finding the shortest path between two nodes in a graph 
is almost always done using BFSclass Solution

'''


# Unit Weight method
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] != 0:
            return -1

        queue = collections.deque()
        queue.append((0,0))

        dist = [[math.inf for _ in range(n)] for _ in range(m)]

        dist[0][0] = 1

        directions = [(0,1), (0,-1), (1,0), (-1, 0), (1,1), (-1,1), (1,-1), (-1,-1)]

        while queue:
            row, col = queue.popleft()
            
            # If we have reached the destination
            if row == m - 1 and col == n - 1:
                return dist[row][col]

            for u,v in directions:
                nei_r = row + u
                nei_c = col + v

                # if nei is out of bound or cant be visited
                if nei_r < 0 or nei_c < 0 or nei_r >= m or nei_c >= n or grid[nei_r][nei_c] != 0:
                    continue
                
                
                nei_dst = dist[row][col] + 1

                if nei_dst < dist[nei_r][nei_c]:
                    queue.append((nei_r, nei_c))
                    dist[nei_r][nei_c] = nei_dst
        
        return -1


# -------------------------------------- Heap   ------------------------------------------------------------------
import heapq
import math
import collections
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] != 0:
            return -1

        minHeap = []
        heapq.heapify(minHeap)

        heapq.heappush(minHeap, (1, 0, 0)) # Dist, row , col

        dist = [[math.inf for _ in range(n)] for _ in range(m)]
        visited = [[False for _ in range(n)] for _ in range(m)]

        directions = [(0,1), (0,-1), (1,0), (-1, 0), (1,1), (-1,1), (1,-1), (-1,-1)]

        while minHeap:
            dst , row, col = heapq.heappop(minHeap)
            
            if visited[row][col] == True:
                continue
            

            visited[row][col] = True
            dist[row][col] = dst

            # If we have reached the destination
            if row == m-1 and col == n-1:
                return dist[row][col]

            for u,v in directions:
                nei_r = row + u
                nei_c = col + v

                # if nei is out of bound or cant be visited
                if nei_r < 0 or nei_c < 0 or nei_r >= m or nei_c >= n or grid[nei_r][nei_c] != 0 or visited[nei_r][nei_c] == True:
                    continue
                
                
                nei_dst = dst + 1
                heapq.heappush(minHeap, (nei_dst, nei_r, nei_c)) # Dist, row , col

                
        
        return -1
        
# ------------------------------- Dijkstra's ------------------------------------------------------------------
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] != 0:
            return -1

        minHeap = []
        heapq.heapify(minHeap)

        heapq.heappush(minHeap, (1, 0, 0)) # Dist, row , col

        dist = [[math.inf for _ in range(n)] for _ in range(m)]
        dist[0][0] = 1

        directions = [(0,1), (0,-1), (1,0), (-1, 0), (1,1), (-1,1), (1,-1), (-1,-1)]

        while minHeap:
            dst , row, col = heapq.heappop(minHeap)

            # If we have reached the destination
            if row == m-1 and col == n-1:
                return dist[row][col]

            for u,v in directions:
                nei_r = row + u
                nei_c = col + v

                # if nei is out of bound or cant be visited
                if nei_r < 0 or nei_c < 0 or nei_r >= m or nei_c >= n or grid[nei_r][nei_c] != 0 or dist[nei_r][nei_c] != math.inf:
                    continue
                
                
                nei_dst = dst + 1

                if nei_dst < dist[nei_r][nei_c]:
                    dist[nei_r][nei_c] = nei_dst
                    heapq.heappush(minHeap, (nei_dst, nei_r, nei_c)) # Dist, row , col
     
        
        return -1