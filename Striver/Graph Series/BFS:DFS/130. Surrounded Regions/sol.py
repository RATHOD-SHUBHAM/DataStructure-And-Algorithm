# from the border keep track of the O adn mark them. 
# after tarversal is complete, check if the board was any unvisited O. this basically say they are surrouned by X and convert them to X

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        top = 0
        left = 0

        right = len(board[0]) - 1
        bottom = len(board) - 1
        
        
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        
        # traverse the borders
        
        # top border
        for col in range(top, right + 1):
            if visited[top][col] == False and board[top][col] == "O":
                self.dfs(top, col, m, n, board, visited)
                
        # Left border
        for row in range(top, bottom + 1):
            if visited[row][left] == False and board[row][left] == "O":
                self.dfs(row, left, m, n, board, visited)
                
        # bottom border
        for col in range(top, right + 1):
            if visited[bottom][col] == False and board[bottom][col] == "O":
                self.dfs(bottom, col, m, n, board, visited)
                
        # right border
        for row in range(top, bottom + 1):
            if visited[row][right] == False and board[row][right] == "O":
                self.dfs(row, right, m, n, board, visited)
                
        # print(visited)
        
        # start marking the cell
        for i in range(m):
            for j in range(n):
                
                if board[i][j] == "O" and visited[i][j] == False:
                    board[i][j] = "X"
                    
        return board
                
                
    def dfs(self, i, j, m, n, board, visited):
        if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] == True or board[i][j] == 'X':
            return
        
        # mark the node as visited
        visited[i][j] = True
        
        # traverse in 4 direction
        top = self.dfs(i - 1, j, m, n, board, visited)
        down = self.dfs(i + 1, j, m, n, board, visited)
        left = self.dfs(i, j - 1, m, n, board, visited)
        right = self.dfs(i, j + 1, m, n, board, visited)
        
        return
        