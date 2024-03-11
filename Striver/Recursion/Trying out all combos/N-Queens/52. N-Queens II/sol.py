class Solution:
    def __init__(self):
        self.count = 0
        self.finalBoard = []

    def totalNQueens(self, n: int) -> int:
        queenTracker = [None] * n

        row = 0
        board = [[] for _ in range(n)]
        self.backTrack(row, queenTracker, board, n)

        print(self.finalBoard)
        return self.count
    
    def backTrack(self, row, queenTracker, board, n):
        if row == n:
            self.buildBoard(queenTracker, board, n)
            self.count += 1
            return
        
        for col in range(n):
            if self.isPossiblePlacement(row, col, queenTracker):
                queenTracker[row] = col
                self.backTrack(row + 1, queenTracker, board, n)
                queenTracker[row] = None

        return
    
    def isPossiblePlacement(self, row, col, queenTracker):
        for prevRow in range(row):
            prevCol = queenTracker[prevRow]

            sameCol = False
            if col == prevCol:
                sameCol = True
            
            sameDiagonal = False
            if abs(row - prevRow) == abs(col - prevCol):
                sameDiagonal = True
            
            if sameCol or sameDiagonal:
                return False
        
        return True
    
    def buildBoard(self, queenTracker, board, n):
        for row in range(len(queenTracker)):
            col = queenTracker[row]
            remaining_col = n - col - 1

            board[row] = '.'*col + 'Q' + '.'*remaining_col
        
        self.finalBoard.append(board.copy())
        return