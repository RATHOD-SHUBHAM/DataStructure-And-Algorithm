"""
Question Simplifies:

If there is "O" in the border, we cannot replace it with "X"

Rest apart, everything else gets replaced with "X"

Logic:

Capture "O's" on the border, and change it to -1

Then traverse the matrix again and replace everything as "X", except -1
replace -1 as "O"
"""
# Tc and Sc: O(m * n)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        # Step 1: Capture "O" from border and replace then with -1
        for col in range(n):
            # First row
            self.dfs(0, col, directions, board, m, n)
            
            # Last row
            self.dfs(m-1, col, directions, board, m, n)
        
        for row in range(m):
            # First Column
            self.dfs(row, 0, directions, board, m, n)
            
            # Last Column
            self.dfs(row, n-1, directions, board, m, n)


        # Step 2: Traverse and fill the region
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
        
        return board
    
    def dfs(self, i, j, directions, board, m, n):
        # base case
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] == "X" or board[i][j] == -1:
            return
        
        # Flip "O" -> -1
        board[i][j] = -1

        for nei in directions:
            nei_i = i + nei[0]
            nei_j = j + nei[1]

            self.dfs(nei_i, nei_j, directions, board, m, n)
        
        return