class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        queue = collections.deque()

        neighbors = [[0,1], [0,-1], [1,0], [-1,0]]

        # If the src is already the same as the target color. Therefore, no changes are made to the image.
        if image[sr][sc] == color:
            return image
        
        # Color the source
        start_color = image[sr][sc]
        self.dfs(sr, sc, start_color, neighbors, color, image, m, n)

        return image
    
    def dfs(self, sr, sc, start_color, neighbors, color, image, m, n):
        # If neighbors dont shares the same color as the starting pixel.
        if sr < 0 or sc < 0 or sr >= m or sc >= n or image[sr][sc] != start_color:
            return
        
        # Color the cell
        image[sr][sc] = color

        for nei in neighbors:
            nei_i = sr + nei[0]
            nei_j = sc + nei[1]

            self.dfs(nei_i, nei_j, start_color, neighbors, color, image, m, n)
        
        return