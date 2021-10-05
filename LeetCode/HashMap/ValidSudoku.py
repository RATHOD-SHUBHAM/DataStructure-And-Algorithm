'''
36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # return a bool value
        # create sets for row,column and each block
        row, col, block = set(), set(), set()

        # loop through each column and each row (9 x 9) to check if the value is uniquely presesnt
        for i in range(9):
            for j in range(9):
                if (board[i][j] != '.'):
                    # create unique set value for each element in row column and that block
                    row_set = (i, board[i][j])
                    col_set = (j, board[i][j])
                    block_set = (i // 3, j // 3, board[i][j])

                    # check if the set are unique in each row and column and block

                    if ((row_set in row) or (col_set in col) or (block_set in block)):
                        return False

                    row.add(row_set)
                    col.add(col_set)
                    block.add(block_set)

        return True

