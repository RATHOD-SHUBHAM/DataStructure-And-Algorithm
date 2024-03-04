class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        n = len(board)
        isValid = self.backTrack(n, board)

        if isValid:
            return True
        else:
            return False
    
    def backTrack(self, n, board):
        for i in range(n):
            for j in range(n):
                if board[i][j] != ".":
                    continue
                
                for number in range(1, 10):
                    number = str(number)

                    if self.isValidPlacment(number, i, j, board, n):
                        board[i][j] = number

                        #backTrack
                        isValid = self.backTrack(n, board)
                        
                        if isValid:
                            return True
                        
                        board[i][j] = '.'

                return False
        
        return True

    def isValidPlacment(self, number, row, col, board, n):
        # traverse all the 9 row and col
        for i in range(n):
            if board[row][i] == number:
                return False
            if board[i][col] == number:
                return False
            # traverse the subcell
            if board[3 * (row //3) + i // 3][3 * (col // 3) + i % 3] == number:
                return False
            
        return True
