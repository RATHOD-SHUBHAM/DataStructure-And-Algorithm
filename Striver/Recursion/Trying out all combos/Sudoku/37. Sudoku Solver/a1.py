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


# ----------------------------------------------------------------------------------------------------------------
    
from collections import defaultdict
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        
        # Step 1: Add the values to dictionary
        set_row, set_col, subset_board = self.createDict(board, n)
        # print(set_row, set_col, subset_board)

        # Step 2: Perform backtracking
        row = 0
        col = 0
        return self.backTrack(row, col, set_row, set_col, subset_board, board, n)
    
    def createDict(self, board, n):
        set_row = defaultdict(set)
        set_col = defaultdict(set)
        subset_board = defaultdict(set)

        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    continue

                cur_number = int(board[i][j])

                set_row[i].add(cur_number)
                set_col[j].add(cur_number)
                subset_board[(i // 3, j // 3)].add(cur_number)    
        
        return set_row, set_col, subset_board
    
    def backTrack(self, row, col, set_row, set_col, subset_board, board, n):
        # base case
        if row == n - 1 and col == n:
            # reached the last cell
            return True
        
        # if col goes outside index, move to next row
        if col == n:
            row += 1
            col = 0
            return self.backTrack(row, col, set_row, set_col, subset_board, board, n)
        
        # If number already exist - move to next col
        if board[row][col] != '.':
            return self.backTrack(row, col + 1, set_row, set_col, subset_board, board, n)
        
        # Fill number
        for number in range(1, 10):
            if self.isValidPlacment(number, row, col,  set_row, set_col, subset_board):
                # add the number
                board[row][col] = str(number)

                # add to set
                set_row[row].add(number)
                set_col[col].add(number)
                subset_board[(row // 3, col // 3)].add(number)

                if self.backTrack(row, col + 1, set_row, set_col, subset_board, board, n):
                    return True
                
                # remove number from set
                set_row[row].remove(number)
                set_col[col].remove(number)
                subset_board[(row // 3, col // 3)].remove(number)

                # remove number from baord
                board[row][col] = '.'
        
        return False


    def isValidPlacment(self, number, row, col, set_row, set_col, subset_board):
        if number in set_row[row] or number in set_col[col] or number in subset_board[(row // 3, col // 3)]:
            return False
        
        return True