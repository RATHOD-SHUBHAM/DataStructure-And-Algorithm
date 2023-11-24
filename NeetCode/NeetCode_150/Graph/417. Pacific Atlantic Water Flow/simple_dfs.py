'''
Same dfs solution writtern in a simple way

'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pacific = set()
        atlantic = set()

        # since we know from top and left pacific can be reached and bottom and right atlantic can be reached - we start our search from there
        for col in range(n):
            # top row
            self.dfs(0, col, heights[0][col], pacific, heights, m, n)
            # Bottom row
            self.dfs(m-1, col, heights[m-1][col], atlantic, heights, m, n)
        
        for row in range(m):
            # Left Col
            self.dfs(row, 0, heights[row][0], pacific, heights, m, n)
            # Right Col
            self.dfs(row, n-1, heights[row][n-1], atlantic, heights, m, n)
        
        # Grab the common cell
        result = []
        for i in range(m):
            for j in range(n):
                if (i,j) in pacific and (i,j) in atlantic:
                    result.append([i,j])

        # print(result)
        return result

    
    def dfs(self, row, col, prevCell, visited, heights, m, n):
        if (row < 0 or row >= m or col < 0 or col >= n or (row, col) in visited 
            or
            heights[row][col] < prevCell # current_cell < prevCell
        ):
            return 
        
        visited.add((row,col))

        # Traverse in 4 direction
        # Up
        self.dfs(row - 1, col, heights[row][col], visited, heights, m, n)
        # Down
        self.dfs(row + 1, col, heights[row][col], visited, heights, m, n)
        # left
        self.dfs(row, col - 1, heights[row][col], visited, heights, m, n)
        # right
        self.dfs(row, col + 1, heights[row][col], visited, heights, m, n)

        return