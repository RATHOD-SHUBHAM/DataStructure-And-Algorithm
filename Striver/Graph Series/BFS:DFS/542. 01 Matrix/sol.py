# Tc :O(m * n) | Sc: O(m * n) 

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        directions = [[-1,0], [1,0], [0,-1], [0,1]]


        minDist = [[math.inf] * n for _ in range(m)]
        visited = [[False] * n for _ in range(m)]
        queue = []

        '''
            1. Cell with value zero - will have dist zero
            2. Mark the cell with dist 0 as visited
            3. Add them to the  queue
        '''
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    minDist[i][j] = 0
                    visited[i][j] = True
                    queue.append((0, i, j)) # dist , cell

        # BFS
        while queue:
            dist , row, col = queue.pop(0)

            for adj_row, adj_col in directions:
                nei_row = adj_row + row
                nei_col = adj_col + col

                if nei_row < 0 or nei_row >= m or nei_col < 0 or nei_col >= n or visited[nei_row][nei_col] == True:
                    continue
                
                # this is a cell with value 1 which hasnt been visited
                new_dist = dist + 1
                visited[nei_row][nei_col] = True

                minDist[nei_row][nei_col] = new_dist

                queue.append((new_dist, nei_row, nei_col))
                
        
        return minDist
                    
                    