'''
    Main Idea is to check if water can flow to current cell from adjacent cell
    and not
    if water can flow from cuurent cell to adjacent cell
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        # Visited
        pacific = set()
        atlantic = set()

        # We can reach pacific and atlantic from top, left, right, bottom border
        
        # from the top rows every col to every other cell : check if i can reach pacific
        # similarly form bottom rows every col to every other cell: check if we can reach every cell

        # since we know from top and left pacific can be reached and bottom and right atlantic can be reached - we start our search from there.
        
        for col in range(n):
            # Top row - check if we can reach pacific
            self.dfs(0, col, m, n, pacific, heights[0][col], heights)
            # Bottom row - check if we can reach atlantic
            self.dfs(m-1, col, m, n, atlantic, heights[m-1][col], heights)
        
        for row in range(m):
            # Left Col - check if we can reach pacific
            self.dfs(row, 0, m, n, pacific, heights[row][0], heights)
            # Right Col - check if we can reach atlantic
            self.dfs(row, n-1, m, n, atlantic, heights[row][n-1], heights)

        result = self.getCommon(pacific, atlantic, m, n )

        return result

    def dfs(self, row, col, m, n, visited, prevHeight, heights):
        '''
            We are checking can water flow from current height to prev Height
            height[row][col] >= prevheight
        '''
        if (
            row < 0 or row >= m or
            col < 0 or col >= n or
            # check if from current height we can flow to previous height
            heights[row][col] < prevHeight or
            (row, col) in visited
        ):
            return

        visited.add((row, col))

        # look for neighbor cells
        # Up
        self.dfs(row - 1, col, m, n, visited, heights[row][col], heights)
        # Down
        self.dfs(row + 1, col, m, n, visited, heights[row][col], heights)
        # left
        self.dfs(row, col - 1, m, n, visited, heights[row][col], heights)
        # right
        self.dfs(row, col + 1, m, n, visited, heights[row][col], heights)

    def getCommon(self, pacific, atlantic, m, n):
        result = []

        for i in range(m):
            for j in range(n):
                if (i,j) in pacific and (i,j) in atlantic:
                    result.append([i,j])
        
        return result