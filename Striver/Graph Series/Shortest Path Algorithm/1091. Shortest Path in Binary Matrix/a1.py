'''
Finding the shortest path between two nodes in a graph 
is almost always done using BFSclass Solution

'''


# Unit Weight method
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0,0], [0,1], [1,-1], [1,0],[1,1]]

        queue = [[1, 0, 0]] # wt, row, col

        while queue:
            dist , row, col = queue.pop(0)

            if row == n-1 and col == n-1:
                return dist
            
            for direction in directions:
                adj_row, adj_col = direction

                nei_row = adj_row + row
                nei_col = adj_col + col

                if nei_row < 0 or nei_row >= n or nei_col < 0 or nei_col >= n or grid[nei_row][nei_col] == 1 or visited[nei_row][nei_col] == True:
                    continue
                
                new_dist = 1 + dist
                visited[nei_row][nei_col] = True
                queue.append([new_dist, nei_row, nei_col])
        
        # If the last cell can be reached
        return -1


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Heap - Dijkstras

# Unit Weight method
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0,0], [0,1], [1,-1], [1,0],[1,1]]

        minHeap = []
        heapq.heapify(minHeap)

        heapq.heappush(minHeap, [1, 0, 0]) # wt, row, col

        while minHeap:
            dist , row, col = heapq.heappop(minHeap)

            if row == n-1 and col == n-1:
                return dist
            
            for direction in directions:
                adj_row, adj_col = direction

                nei_row = adj_row + row
                nei_col = adj_col + col

                if nei_row < 0 or nei_row >= n or nei_col < 0 or nei_col >= n or grid[nei_row][nei_col] == 1 or visited[nei_row][nei_col] == True:
                    continue
                
                new_dist = 1 + dist
                visited[nei_row][nei_col] = True
                heapq.heappush(minHeap, [new_dist, nei_row, nei_col])
        
        # If the last cell can be reached
        return -1

        