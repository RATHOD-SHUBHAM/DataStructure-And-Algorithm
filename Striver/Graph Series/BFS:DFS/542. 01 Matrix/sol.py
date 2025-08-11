# Tc :O(m * n) | Sc: O(m * n) 

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        visited = [[False for _ in range(n)] for _ in range(m)]

        dist = [[math.inf for _ in range(n)] for _ in range(m)]

        '''
            1. Cell with value zero - will have dist zero
            2. Mark the cell with value zero as visited
            3. Add them to the  queue
        '''
        queue = collections.deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    visited[i][j] = True
                    dist[i][j] = 0
                    queue.append((0, i, j)) # Dist, Coords
        
        # Explore neighbors of cell with value zero
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        while queue:
            dst, i, j = queue.popleft()

            for nei in directions:
                nei_i = i + nei[0]
                nei_j = j + nei[1]

                if nei_i < 0 or nei_j < 0 or nei_i >= m or nei_j >= n or mat[nei_i][nei_j] == 0 or visited[nei_i][nei_j] == True:
                    continue
                
                visited[nei_i][nei_j] = True

                new_dst = 1 + dst
                dist[nei_i][nei_j] = new_dst

                queue.append((new_dst, nei_i, nei_j)) # Dist, Coords
        
        return dist