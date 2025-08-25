class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        # Memoization
        cost = [[-math.inf for _ in range(n)] for _ in range(m)] # Keep track of longest path for each node

        LIP = -math.inf
        for i in range(m):
            for j in range(n):
                # If the cell is already traversed, then it is part of some path
                if cost[i][j] != -math.inf:
                    continue
                
                path_len = self.dfs(i, j, cost, directions, matrix, m, n)

                LIP = max(LIP, path_len)
        
        # print(cost)
        return LIP

    def dfs(self, row, col, cost, directions, mat, m , n):
        # Explore all the neighbor and find the max path
        path_len = 0
        for adj_row, adj_col in directions:
            nei_row = adj_row + row
            nei_col = adj_col + col

            if nei_row < 0 or nei_row >= m or nei_col < 0 or nei_col >= n or mat[row][col] >= mat[nei_row][nei_col]:
                continue
            
            if cost[nei_row][nei_col] == -math.inf:
                cur_len = self.dfs(nei_row, nei_col, cost, directions, mat, m, n)
            else:
                cur_len = cost[nei_row][nei_col]
            
            path_len = max(path_len, cur_len) 

        cost[row][col] = 1 + path_len
        return cost[row][col]