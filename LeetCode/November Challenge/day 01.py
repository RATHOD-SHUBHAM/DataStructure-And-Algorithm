'''

130. Surrounded Regions

Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
Example 2:

Input: board = [["X"]]
Output: [["X"]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.

'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        Dont flip the cell the is not surrounded by X
        Flip all then remaining cells.
        
        https://www.youtube.com/watch?v=9z2BunfoZ5Y
        
        3 steps:
        
        1. Capture the O cells that are not surrounded by X and flip it to T.
        2. Flip everything to X except for T
        3. Flip back the T to X
        
        Time compexity: O(N * M), where N is the height of the board and M is the             width of the board. Since in the wrost case algorithm processes all cells             twice and O(2 * N * M) == O(N * M)
        Space complexity: O(N * M)
        
        """
        row = len(board)
        col = len(board[0])
        
        #step 1:  (DFS) Capture Unsurrounded region ( O -> T ):
        def capture(r,c):
            if (r < 0 or c < 0 or r == row or c == col or board[r][c] != 'O'):
                return
            
            board[r][c] = 'T'
            capture(r - 1,c)
            capture(r + 1,c)
            capture(r , c + 1)
            capture(r , c - 1)
        
        # DFS
        for r in range(row):
            for c in range(col):
                # if you find a 'o' in border convert it to 'T'
                if board[r][c] == 'O' and (r in [0, row-1] or c in [0,col-1]):
                    # capture(r,c)
                    board[r][c] = 'T'
                    
        #step 2: Capture the surrunded area (O -> X)
        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                    
        # step 3: Convert the T back to O
        for r in range(row):
            for c in range(col):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                    