# Tc :O(m * n) | Sc: O(m * n) 
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        distance = [[0 for _ in range(n)] for _ in range(m)]
        
        queue = []
        
        # get the cell with 0 value and mark them as visited
        for i in range(m):
            for j in range(n):
                
                if mat[i][j] == 0:
                    queue.append([i, j, 0]) #inital distace is 0
                    visited[i][j] = True
                    
        
        # get the distance of other cell from initial cell and so on
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        
        while queue:
            r , c , dist = queue.pop(0)
            
            for adj_r, adj_c in directions:
                nr = r + adj_r
                nc = c + adj_c
                
                if 0 <= nr < m and 0 <= nc < n and visited[nr][nc] == False:
                    if mat[nr][nc] == 1:
                        visited[nr][nc] = True
                        new_dist = dist + 1
                        distance[nr][nc] = new_dist
                        
                        queue.append([nr, nc, new_dist])
        

        return distance
                    
                    