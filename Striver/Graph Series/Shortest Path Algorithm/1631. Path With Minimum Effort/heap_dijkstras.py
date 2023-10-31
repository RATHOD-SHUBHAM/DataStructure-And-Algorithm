# Calculate the minimum effort required for each cell and slowly move toward destination

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])

        # store the minimum effort of all cell
        min_effort = [[math.inf] * n for _ in range(m)]
        min_effort[0][0] = 0

        visited = [[False] * n for _ in range(m)]

        minHeap = []
        heapq.heapify(minHeap)

        # path effort, row, col
        heapq.heappush(minHeap, (0,0,0))

        directions =  [(0,-1), (0,1), (-1, 0), (1, 0)]


        while minHeap:
            max_path_effort, row, col = heapq.heappop(minHeap)

            if row == m - 1 and col == n - 1:
                return max_path_effort # this will be the minimum effort to reach the destination
            
            cur_height = heights[row][col]
            visited[row][col] = True

            for direction in directions:
                adj_row , adj_col = direction

                nei_row = adj_row + row
                nei_col = adj_col + col

                if nei_row < 0 or nei_row >= m or nei_col < 0 or nei_col >= n or visited[nei_row][nei_col] == True:
                    continue
                

                nei_height = heights[nei_row][nei_col]
                cur_path_difference = abs(cur_height - nei_height)

                # maximum route effort
                max_route_effort  = max(max_path_effort , cur_path_difference)


                # check and update the min effort
                if max_route_effort < min_effort[nei_row][nei_col]:
                    min_effort[nei_row][nei_col] = max_route_effort
                    heapq.heappush(minHeap, (max_route_effort,nei_row, nei_col))