class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        # Explore boarders 
        # top boarder and bottom boarder
        for col in range(n):
            self.dfs(0, col, board, m , n)
            self.dfs(m-1, col, board, m, n)
        
        # print(board)

        # Left and right boarder
        for row in range(m):
            self.dfs(row, 0 , board, m , n)
            self.dfs(row, n-1, board, m , n)

        # print(board)

        # change the cell to 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == -1:
                    board[i][j] = 'O'
        return board

        

    def dfs(self, row, col, board, m , n):
        if row < 0 or row >= m or col < 0 or col >= n or board[row][col] == 'X' or board[row][col] == -1:
            return
        
        board[row][col] = -1

        # traverse in 4 direction
        self.dfs(row - 1, col , board, m , n) # top
        self.dfs(row + 1, col , board, m , n) # down
        self.dfs(row, col - 1 , board, m , n) # left
        self.dfs(row, col + 1, board, m , n) # right

        return