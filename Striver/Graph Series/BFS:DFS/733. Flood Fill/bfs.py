class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        # If the starting cell is already colored
        if image[sr][sc] == color:
            return image

        directions = [(-1, 0), (1,0), (0,-1), (0,1)]
        
        queue = [[sr, sc]]

        start_color = image[sr][sc]

        while queue:
            row, col = queue.pop(0)

            # Color the cell
            image[row][col] = color

            for adj_row, adj_col in directions:
                nei_row = adj_row + row
                nei_col = adj_col + col

                if nei_row < 0 or nei_col < 0 or nei_row >= m or nei_col >= n or image[nei_row][nei_col] != start_color or image[nei_row][nei_col] == color:
                    continue
                
                queue.append([nei_row, nei_col])

        return image