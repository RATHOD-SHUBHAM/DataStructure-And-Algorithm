'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.

'''

# Time: O(n^2)
# Space: O(n^2)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9 # we know this is a 9 x 9 Matrix
        
        # Create 3 dictionary --> For row , col and for nine 3 x 3 sub-boxes
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        subBox = collections.defaultdict(set)
        
        
        # print("rows dict: ", rows)
        # print("cols dict: ",cols)
        # print("subBox dict: ",subBox)
        
        
        for row in range(n):
            # print("\n")
            # print("row is {}".format(row))
            for col in range(n):
                # print("col is {}".format(col))
                if board[row][col] == ".":
                    # print(row,col)
                    continue
                if(board[row][col] in rows[row] or
                  board[row][col] in cols[col] or
                  board[row][col] in subBox[(row // 3 , col // 3)]):
                    return False
                
                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                subBox[(row // 3 , col // 3)].add(board[row][col])
                
#                 print("rows dict: ", rows)
#                 print("cols dict: ",cols)
#                 print("subBox dict: ",subBox)
                
#                 print("\n")
                
        return True