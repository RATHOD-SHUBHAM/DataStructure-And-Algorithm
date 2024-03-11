class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # creating a board
        ans = []
        Finalboard = [[] for _ in range(n)]
        
        # each index is considered to be a row
        queenTracker = [0] * n # keep track of col in which queen is placed
        validPositionCount = self.validate(0 , n , queenTracker,Finalboard,ans)

        # print(validPositionCount)
        
        return ans
    
    def validate(self,row,n,queenTracker,Finalboard,ans):
        # base case: when i move out of the last row. I have finished placing every queen in right position.
        if row == n:
            self.board(queenTracker,Finalboard,n,ans)
            return 1 # just to 
        
        validPositionCount = 0 # keep count of how many valid posiiton are there
        
        for col in range(n):
            if self.isValidPosition(row,col,queenTracker):
                queenTracker[row] = col # add queen to current position
                validPositionCount +=  self.validate(row+1,n,queenTracker,Finalboard,ans)
                queenTracker[row] = 0 # remove queen from current position
 
        return validPositionCount
    
    # check if there are no queen in particular col and in diagonal col
    def isValidPosition(self,row,col,queenTracker):
        for previousRow in range(row):
            colToCheck = queenTracker[previousRow]
            
            # check if they are in same col
            sameCol = False
            if col == colToCheck:
                sameCol = True
            '''
            This can be written as
            sameCol = (col == colToCheck)
            '''

            # check diagonal => abs(x2 - x1) = abd(y2 - y1)
            sameDiagonal = False
            if abs(col - colToCheck) == abs(row - previousRow):
                sameDiagonal = True
            
            '''
            This can be written as
            sameDiagonal = abs(col - colToCheck) == abs(row - previousRow)
            '''

            if sameCol or sameDiagonal:
                return False
            
        return True
    
    
    def board(self,queenTracker,Finalboard,n,ans):
        for row in range(len(queenTracker)):
            # print("row : ",row)
            # print("col : ",queenTracker[row])
            # print("pos in board : ",n-(queenTracker[row]) -1)
            Finalboard[row] = '.'*(queenTracker[row]) + 'Q' + '.'*(n-(queenTracker[row]) -1 )
        # print(Finalboard)
        # copy = Finalboard[:]
        # ans.append(copy)
        # print("ans: ",ans)
        ans.append(Finalboard.copy())
        
        return ans
    

# ------------------------------------------------------------------------------------------
    
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