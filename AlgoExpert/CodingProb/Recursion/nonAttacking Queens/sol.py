class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        all_board = []
        final_board = [["."] * n for _ in range(n)]
        
        row  = 0
        
        blocked_col = set()
        blocked_diagonal_left =set()
        blocked_diagonal_right = set()
        
        count = self.placeQueens(row, n, blocked_col, blocked_diagonal_left, blocked_diagonal_right, final_board, all_board)
        
        return all_board
    
    def placeQueens(self, row, n, blocked_col, blocked_diagonal_left, blocked_diagonal_right, final_board, all_board):
        
        # base case: when we reach the end of board
        if row == n:
            all_board.append(self.buildQueen(final_board))
            return
        
        # go through each col and check if this is the right place
        count = 0
        for col in range(n):
            # check if this is a validPosition to place the queen
            if self.isValid(row, col, blocked_col, blocked_diagonal_left, blocked_diagonal_right):

                # Diagonal Values
                right_diagonal_value = row - col
                left_diagonal_value = row + col
                
                
                # place the queen at this position and block the position for next queen
                final_board[row][col] = "Q"
                blocked_col.add(col)
                
                # blocking the sides of diagonals
                blocked_diagonal_left.add(left_diagonal_value)
                blocked_diagonal_right.add(right_diagonal_value)
                
                # move to the next row
                count += self.placeQueens(row + 1, n, blocked_col, blocked_diagonal_left, blocked_diagonal_right, final_board, all_board)
                
                # remove the queen from current position and check for next position
                final_board[row][col] = "."
                blocked_col.remove(col)
                # removing the blocked diagonals
                blocked_diagonal_left.remove(left_diagonal_value)
                blocked_diagonal_right.remove(right_diagonal_value)
                
        return
    
    def isValid(self,row, col, blocked_col, blocked_diagonal_left, blocked_diagonal_right):
        right_diagonal_value = row - col
        left_diagonal_value = row + col
        
        if col in blocked_col or right_diagonal_value in blocked_diagonal_right or left_diagonal_value in blocked_diagonal_left:
            return False
        else:
            return True
    
    
    def buildQueen(self, final_board):
        board = []
        
        # print("final_board: ",final_board)
        for row in final_board:
            board.append("".join(row))
        
        # print("board: ",board)
        return board