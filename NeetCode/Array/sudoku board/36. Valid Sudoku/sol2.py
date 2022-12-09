# Time and Sc: O(N^2)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9 # size of the board
        
        set_row =[set() for _ in range(N)]
        set_col =[set() for _ in range(N)]
        set_board =[set() for _ in range(N)]
        
        for row in range(N):
            for col in range(N):
                val = board[row][col]
                
                if val == ".":
                    continue
                    
                # check if the cur row set has this value
                if val in set_row[row]:
                    return False
                set_row[row].add(val)
                
                # check if the cur col set has this value
                if val in set_col[col]:
                    return False
                set_col[col].add(val)
                
                # check if the cur board has this value
                idx = (row // 3) * 3 + (col // 3)
                
                if val in set_board[idx]:
                    return False
                set_board[idx].add(val)
        
        return True
        
        
        