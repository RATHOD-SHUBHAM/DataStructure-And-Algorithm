# Tc and Sc: O(m * n)

# BFS

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
        image[sr][sc] = color
        queue.append((sr,sc))

        while queue:
            i, j = queue.popleft()

            for nei in neighbors:
                nei_i = i + nei[0]
                nei_j = j + nei[1]

                # If neighbors dont shares the same color as the starting pixel.
                if nei_i < 0 or nei_j < 0 or nei_i >= m or nei_j >= n or image[nei_i][nei_j] != start_color:
                    continue
                
                # Color the neighbors
                image[nei_i][nei_j] = color
                queue.append((nei_i, nei_j))

        return image

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# DFS

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

        