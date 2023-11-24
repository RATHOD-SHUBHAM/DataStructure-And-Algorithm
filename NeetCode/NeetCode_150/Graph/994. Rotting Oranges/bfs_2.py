class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        directions = [[-1,0], [1,0], [0,-1], [0,1]]

        fresh_oranges = 0
        queue = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    queue.append([i, j, 0])
        

        max_time = 0
        while queue:
            row, col , time = queue.pop(0)
            max_time = max(max_time, time)

            for adj_row, adj_col in directions:
                nei_row = adj_row + row
                nei_col = adj_col + col

                if nei_row < 0 or nei_col < 0 or nei_row >= m or nei_col >= n or grid[nei_row][nei_col] != 1:
                    continue

                fresh_oranges -= 1
                grid[nei_row][nei_col] = 2
                queue.append([nei_row, nei_col , time + 1])

        
        # print(max_time)
        if fresh_oranges == 0:
            return max_time
        else:
            return -1