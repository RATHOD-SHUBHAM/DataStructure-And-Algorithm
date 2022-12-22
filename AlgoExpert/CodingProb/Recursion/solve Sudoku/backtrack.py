class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        
        set_row = [set() for _ in range(n)]
        set_col = [set() for _ in range(n)]        
        set_board = [set() for _ in range(n)]
        
        # add all the existing number in board to the set
        for row in range(n):
            for col in range(n):
                if board[row][col] == ".":
                    continue
                
                val = int(board[row][col])
                
                # add them in set to check for unique value
                set_row[row].add(val)
                set_col[col].add(val)
                
                box_idx = (row // 3) * 3 + (col // 3)
                set_board[box_idx].add(val)
                
        # start at (0,0)
        cur_row = 0
        cur_col = 0
        if self.backtrack(cur_row, cur_col, n , board, set_row, set_col, set_board):
            return board
    
    def backtrack(self, row, col, n , board, set_row, set_col, set_board):
        # todo: base case
        # check if we reached the end of the board
        if row == n-1 and col == n:
            return True
        # if we reached the end of cur row
        elif col == n:
            row += 1
            col = 0
            # self.backtrack(row, col , n , board, set_row, set_col, set_board)
        
        
        # check if the current cell has a number
        if board[row][col] != ".":
            # move to next col
            return self.backtrack(row, col+1 , n , board, set_row, set_col, set_board)
            
        # if the current cell is empty   
        # add number from 1- 9 and check if the sudoku will be formed
        for num in range(1, n+1):
            # check if cur number can be added at this place
            if not self.isValid(num, row, col, set_row, set_col, set_board):
                continue
            
            # if this is a valid place
            board[row][col] = str(num)
            
            # add the number into set
            set_row[row].add(num)
            set_col[col].add(num)

            box_idx = (row // 3) * 3 + (col // 3)
            set_board[box_idx].add(num)
            
            # now move to next cells and check if this is a correct placeholder for cur num
            if self.backtrack(row, col+1 , n , board, set_row, set_col, set_board):
                return True
            
            # if this is not the correct placeholder for cur num
            # move on and check for other number
            # but before that make this cell empty
            board[row][col] = "."
            set_row[row].remove(num)
            set_col[col].remove(num)

            box_idx = (row // 3) * 3 + (col // 3)
            set_board[box_idx].remove(num)
            
        # if none of the number is possible 
        return False
    
    def isValid(self, num, row, col, set_row, set_col, set_board):
        box_idx = (row // 3) * 3 + (col // 3)
    
        if (
            num not in set_row[row] and
            num not in set_col[col] and
            num not in set_board[box_idx]
           ):
            return True
        else:
            return False
        