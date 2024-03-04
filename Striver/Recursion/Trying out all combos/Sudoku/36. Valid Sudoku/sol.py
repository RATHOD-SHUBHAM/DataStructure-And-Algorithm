import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        n = len(board[0])

        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        sub_board = collections.defaultdict(set) # key = (row // 3 , col // 3)

        for i in range(m):
            for j in range(n):
                
                cur_val = board[i][j]

                if cur_val == ".":
                    continue

                if cur_val in row[i] or cur_val in col[j] or cur_val in sub_board[(i // 3, j // 3)]:
                    return False
                

                # add to dictionary
                row[i].add(cur_val)
                col[j].add(cur_val)
                sub_board[(i // 3, j // 3)].add(cur_val)
        
        return True