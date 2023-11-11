'''
    Every cell "O" except the one connected to boundary cannot be turned to "X"
    
    Create a Indicator (which in our case will be visited matrix) which says that , these cells
    cannot  be converted to zero
'''


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        top = 0
        left = 0

        right = n
        bottom = m

        # Indicator
        visited = [[False] * n for _ in range(m)]

        directions = [(1,0), (0,1), (-1, 0), (0, -1)]
        

        # DFS Helper ------------------------------------------------
        def markCell(row, col):
            if row < 0 or col < 0 or row >= m or col >= n or board[row][col] == "X" or visited[row][col] == True:
                return
            
            # mark the cell indicating this cant be converted
            visited[row][col] = True

            for adj_row, adj_col in directions:
                nei_row = adj_row + row
                nei_col = adj_col + col

                markCell(nei_row, nei_col)

            return



        # Main ------------------------------------------------------------

        # Step 1Traverse the borders

        # Top Border
        for col in range(left , right):
            if board[top][col] == "O" and visited[top][col] == False:
                markCell(top, col)
        
        # Bottom Border
        for col in range(left, right):
            if board[bottom - 1][col] == "O" and visited[bottom - 1][col] == False:
                markCell(bottom - 1, col)

        # Left Border
        for row in range(top, bottom):
            if board[row][left] == "O" and visited[row][left] == False:
                markCell(row, left)

        # Right Border
        for row in range(top, bottom):
            if board[row][right - 1] == "O" and visited[row][right - 1] == False:
                markCell(row, right - 1)


        # Step 2: Convert "O" to "X"
        # convert all the cell which indicate that they can be converted

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and visited[i][j] == False:
                    board[i][j] = "X"

        return board
