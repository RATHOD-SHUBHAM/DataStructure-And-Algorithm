class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        visited = [[False for _ in range(n)] for _ in range(m)]
        cost = [[-math.inf for _ in range(n)] for _ in range(m)]


        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]

        # Helper Function
        def dfs(row, col):
            
            # if visited - return the max path from this place
            if visited[row][col] == True and cost[row][col] != -math.inf:
                return cost[row][col]
            
            visited[row][col] = True
            
            # Explore neighbors
            path_cost = 0
            for adj_row, adj_col in directions:
                nei_row = adj_row + row
                nei_col = adj_col + col

                if nei_row < 0 or nei_row >= m or nei_col < 0 or nei_col >= n:
                    continue

                if visited[nei_row][nei_col] == True and cost[nei_row][nei_col] == -math.inf:
                    continue

                if matrix[row][col] >= matrix[nei_row][nei_col]:
                    continue

                cur_cost = dfs(nei_row, nei_col)

                path_cost = max(cur_cost , path_cost) # Select max path from 4 direction
            
            # Update the cost for current cell
            cost[row][col] = 1 + path_cost

            return cost[row][col]



        # Main function
        longest_increasing_path = 1

        for i in range(m):
            for j in range(n):
                # if the node is already visited
                if visited[i][j] == True:
                    longest_increasing_path = max(longest_increasing_path, cost[i][j])
                    continue
                
                path_len = dfs(i, j)

                longest_increasing_path = max(longest_increasing_path, path_len)
        
        return longest_increasing_path