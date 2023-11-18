# Tc and Sc :O(n^2)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        n = len(board[0])

        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        sub_board = collections.defaultdict(set) # key = (row // 3)(col // 3)

        for i in range(m):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                
                # Check for duplicate
                if (
                    board[i][j] in row[i]
                    or
                    board[i][j] in col[j]
                    or
                    board[i][j] in sub_board[(i // 3),(j // 3)]
                ):
                    return False

                # Add to dictionary
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                sub_board[(i // 3),(j // 3)].add(board[i][j])
        
        return True