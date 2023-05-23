class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        m = len(image)
        n = len(image[0])
        
        
        # helper code --------------------------
        def dfs(i, j, color_start_pxl):
            # base case
            if i < 0 or j < 0 or i >= m or j >= n or image[i][j] != color_start_pxl:
                return

            # change the color of current cell to the color they have provided
            image[i][j] = color

            # Move in 4 direction
            dfs(i-1, j, color_start_pxl)
            dfs(i+1, j, color_start_pxl)
            dfs(i, j-1, color_start_pxl)
            dfs(i, j+1, color_start_pxl)

            return
        
        
        # main code --------------------------
        color_start_pxl = image[sr][sc]
        
        if color_start_pxl == color:
            return image
        
        dfs(sr, sc, color_start_pxl)
        
        return image
    
    