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