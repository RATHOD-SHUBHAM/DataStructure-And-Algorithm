"""
Formula to get
1. Sub Cell No : (row // sub_row_size) , (col // sub_row_col)
2. Cell No : (row * No of Col) + col

Formula of row-major-order: 
row-major-order is used to convert 2D into 1D array:
    Cell No : (row * No of Col) + col
"""

# Tc: O(N^2) | Sc: O(N)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = collections.defaultdict(set)
        col_set = collections.defaultdict(set)
        cell_set = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == '.':
                    continue
                
                if (val in row_set[r]) or (val in col_set[c]) or val in cell_set[(r // 3, c // 3)]:
                    return  False
                
                row_set[r].add(val)
                col_set[c].add(val)
                cell_set[(r // 3, c // 3)].add(val)
        
        return True
    

# ------------------------------------ Using Cell No ------------------------------------


"""
Formula of row-major-order: 
row-major-order is used to convert 2D into 1D array:
    Cell No : (row * No of Col) + col
"""

# Tc: O(N^2) | Sc: O(N)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = collections.defaultdict(set)
        col_set = collections.defaultdict(set)
        cell_set = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == '.':
                    continue

                cell_no = (r // 3 * 3) + c // 3
                
                if (val in row_set[r]) or (val in col_set[c]) or val in cell_set[cell_no]:
                    return  False
                
                row_set[r].add(val)
                col_set[c].add(val)
                cell_set[cell_no].add(val)
        
        return True