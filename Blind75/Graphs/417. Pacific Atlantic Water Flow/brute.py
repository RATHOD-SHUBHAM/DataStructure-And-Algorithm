'''
Will give error for this matrix
    [[1,2,3],[8,9,4],[7,6,5]]

But this will give a hint that we need to perform DFS
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pacific = [[False for _ in range(n)] for _ in range(m)]
        atlantic = [[False for _ in range(n)] for _ in range(m)]

        # Filling the top and left for pacific ocean
        for row in range(m):
            pacific[row][0] = True
        for col in range(n):
            pacific[0][col] = True
        
        # Filling the right and bottom for atlantic ocean
        for row in range(m):
            atlantic[row][n-1] = True
        for col in range(n):
            atlantic[m-1][col] = True
        
        # print(pacific)
        # print(atlantic)

        # Can reach pacific - look at top and left cell
        for i in range(1,m):
            for j in range(1,n):
                # grab heights
                cur_cell = heights[i][j]
                top_cell = heights[i-1][j]
                left_cell = heights[i][j-1]

                can_flow = False
                if cur_cell >= top_cell or cur_cell >= left_cell:
                    can_flow = True
                
                # check flow
                top_flow = pacific[i-1][j]
                left_flow = pacific[i][j-1]

                if can_flow and (top_flow or left_flow):
                    pacific[i][j] = True
        # print(pacific)

        # Can reach atlantic - look at bottom and right cell
        for i in reversed(range(m-1)):
            for j in reversed(range(n-1)):
                # grab heights
                cur_cell = heights[i][j]
                bottom_cell = heights[i+1][j]
                right_cell = heights[i][j+1]

                can_flow = False
                if cur_cell >= bottom_cell or cur_cell >= right_cell:
                    can_flow = True
                
                # check flow
                bottom_flow = atlantic[i+1][j]
                right_flow = atlantic[i][j+1]

                if can_flow and (bottom_flow or right_flow):
                    atlantic[i][j] = True
        # print(atlantic)

        # Get the common cell which can flow to both ocean
        result = []
        for i in range(m):
            for j in range(n):
                pacific_ocean = pacific[i][j]
                atlantic_ocean = atlantic[i][j]

                if pacific_ocean and atlantic_ocean:
                    result.append([i,j])
        
        # print(result)
        return result