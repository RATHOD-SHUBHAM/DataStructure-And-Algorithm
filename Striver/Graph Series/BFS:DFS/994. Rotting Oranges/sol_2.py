class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        directions = [(0,-1), (0,1), (1, 0), (-1, 0)]

        # get the count of fresh orange
        fresh_orange = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_orange += 1

        
        # print(fresh_orange)

        # Get the position of rotten oranges at time 0
        stack = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    stack.append((0, i, j)) # Time at which this particular orange was rotten
        
        # print(stack)

        if not stack and fresh_orange == 0:
            return 0

        # Bfs
        time = 0 # global time to keep track when the orange will rot
        while stack:
            t, i , j = stack.pop(0)

            if fresh_orange == 0:
                return time

            for nei in directions:
                adj_row , adj_col = nei

                nei_row = adj_row + i
                nei_col = adj_col + j


                if nei_row < 0 or nei_row >= m or nei_col < 0 or nei_col >= n or grid[nei_row][nei_col] != 1:
                    continue
                
                grid[nei_row][nei_col] = 2 # rotting the orange
                fresh_orange -= 1

                stack.append((t + 1, nei_row, nei_col))

                # this will help return the first time stamp when the last orange will rot
                time = t + 1

        return -1


