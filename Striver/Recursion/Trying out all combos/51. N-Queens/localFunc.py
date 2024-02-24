class Solution:
    def __init__(self):
        
        self.finalBoard = []
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[] for _ in range(n)]

        queenTracker = [0] * n

        row = 0

        validPositionCount = self.validate(row, n , board, queenTracker)

        return self.finalBoard
    
    def validate(self, row, n , board, queenTracker):
        if row == n:
            self.buildBoard(n, queenTracker, board)
            return 1
        
        validPosition = 0

        for col in range(n):
            if self.isValidPosition(row, col, queenTracker):
                # Place queen in current position
                queenTracker[row] = col
                # move to next placement
                validPositionCount = self.validate(row + 1, n , board, queenTracker)
                # remove queen from current position
                queenTracker[row] = 0
        
        return validPosition
    

    def isValidPosition(self, row, col, queenTracker):
        for prevRow in range(row):
            prevCol = queenTracker[prevRow]

            sameCol = False
            if prevCol == col:
                sameCol = True
            
            sameDiagonal = False
            if abs(row - prevRow) == abs(col - prevCol):
                sameDiagonal = True
            
            if sameCol or sameDiagonal:
                return False
        
        return True

    def buildBoard(self, n, queenTracker, board):
        for row in range(len(queenTracker)):
            col = queenTracker[row]
            remaining_pos = n - col - 1
            board[row] = "."*col + 'Q' + "."*remaining_pos
        
        self.finalBoard.append(board[::])

        return