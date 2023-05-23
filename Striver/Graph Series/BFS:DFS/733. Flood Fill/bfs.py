class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        
        # create a duplicate for the input image
        dup_image = [[None for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dup_image[i][j] = image[i][j]
        
        # change the given cell color
        dup_image[sr][sc] = color
        
        # BFS
        queue = [(sr,sc)]
        
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        while queue:
            r, c = queue.pop(0)
            
            for direction in directions:
                nr , nc = direction
                
                nei_r = nr + r
                nei_c = nc + c
                
                if ( nei_r < 0 or nei_c < 0 or nei_r >= m or nei_c >= n or 
                    dup_image[nei_r][nei_c] != image[sr][sc] or
                    dup_image[nei_r][nei_c] == color
                   ):
                    continue
                
                # change the color
                dup_image[nei_r][nei_c] = color
                queue.append((nei_r, nei_c))
        

        return dup_image