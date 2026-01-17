from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        cell_set = defaultdict(set)

        for row in range(9):
            for col in range(9):
                # get the value at each cell
                val = board[row][col]

                # check if it is empty
                if val == '.':
                    continue
                
                # check if this val is duplicate
                if(
                    val in row_set[row] or
                    val in col_set[col] or
                    val in cell_set[(row // 3, col // 3)]
                ):
                    return False

                row_set[row].add(val)
                col_set[col].add(val)
                cell_set[(row // 3, col // 3)].add(val)
        
        return True

        