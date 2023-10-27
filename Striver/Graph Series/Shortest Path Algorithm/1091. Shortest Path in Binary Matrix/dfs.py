# Time Limited Exceeded.

# Unit Weight method + Node Comprehension
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        dist = [[math.inf] * n for _ in range(n)]
        dist[0][0] = 1

        visited = [[False] * n for _ in range(n)]

        directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0,0], [0,1], [1,-1], [1,0],[1,1]]

        # Helper Function ------------------------------------------------------

        def dfs(row, col):
            visited[row][col] == True

            # Explore neighbors
            for direction in directions:
                adj_row, adj_col = direction

                nei_row = row + adj_row
                nei_col = col + adj_col

                # Node Comprehension
                new_dist = dist[row][col] + 1

                if nei_row < 0 or nei_row >= n or nei_col < 0 or nei_col >= n or grid[nei_row][nei_col] == 1 or visited[nei_row][nei_col] == True or new_dist >= dist[nei_row][nei_col]:
                    continue

                dist[nei_row][nei_col] = new_dist

                dfs(nei_row, nei_col)

        # Main Function ------------------------------------------------------

        for row in range(n):
            for col in range(n):

                visited[row][col] == True

                if grid[row][col] == 1:
                    continue

                # Explore neighbors
                for direction in directions:
                    adj_row, adj_col = direction

                    nei_row = row + adj_row
                    nei_col = col + adj_col

                    # Node Comprehension
                    new_dist = dist[row][col] + 1

                    if nei_row < 0 or nei_row >= n or nei_col < 0 or nei_col >= n or grid[nei_row][nei_col] == 1 or visited[nei_row][nei_col] == True or new_dist >= dist[nei_row][nei_col]:
                        continue

                    dist[nei_row][nei_col] = new_dist

                    dfs(nei_row, nei_col)

        # print(dist)
        return -1 if dist[n-1][n-1] == math.inf else dist[n-1][n-1]




