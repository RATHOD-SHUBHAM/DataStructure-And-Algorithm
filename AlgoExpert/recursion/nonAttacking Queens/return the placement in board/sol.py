class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # creating a board
        ans = []
        Finalboard = [[]*n for _ in range(n)]
        
        # each index is considered to be a row
        queenTracker = [0] * n # keep track of col in which queen is placed
        self.validate(0 , n , queenTracker,Finalboard,ans)
        
        return ans
    
    def validate(self,row,n,queenTracker,Finalboard,ans):
        # base case: when i move out of the last row. I have finished placing every queen in right position.
        if row == n:
            self.board(queenTracker,Finalboard,n,ans)
            return 1
        
        validPositionCount = 0
        
        for col in range(n):
            if self.isValidPosition(row,col,queenTracker):
                queenTracker[row] = col
                validPositionCount +=  self.validate(row+1,n,queenTracker,Finalboard,ans)
                
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
        copy = Finalboard[:]
        ans.append(copy)
        # print("ans: ",ans)
        
        return ans