# ======================================================================
# Pre Req: 303. Range Sum Query - Immutable
# ======================================================================

# Brute Frorce Approach
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sumRegion = 0

        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                sumRegion += self.mat[i][j]
        
        return sumRegion
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


# ---------------------------------- ------------------ ------------------- ------------------ -

# Pre Req: 303. Range Sum Query - Immutable

# Prefix Sum : Elobarated
# 304. Range Sum Query 2D - Immutable
# Approach: 2D Prefix Sum (Row-wise then Column-wise)
#
# Core Idea:
# Instead of summing every element in the region each query (O(m*n)),
# precompute a 2D prefix sum matrix so each query is answered in O(1).
#
# Precomputation is done in two passes:
#   Pass 1 — Row-wise prefix sum: mat[row][i] = sum of all elements from col 0 to col i
#   Pass 2 — Col-wise prefix sum: mat[i][col] = sum of all elements from row 0 to row i
#
# After both passes, mat[r][c] = sum of entire rectangle from (0,0) to (r,c)
#
# Query uses inclusion-exclusion to extract any sub-rectangle:
#
#   +------------------+
#   |   top_region     |
#   +--------+---------+
#   |  left  |  target |
#   | region |  region |
#   +--------+---------+
#
#   target = mat[row2][col2] - left_region - top_region + intersection
#
#   Why + intersection?
#   left_region and top_region both INCLUDE the top-left overlapping corner,
#   so it gets subtracted twice — add it back once to compensate.
#
# TC: O(m*n) precomputation, O(1) per query
# SC: O(1) extra space (modifies matrix in-place)
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix

        m = len(self.mat)
        n = len(self.mat[0])

        # Pass 1: Row-wise prefix sum (same as 303 applied to each row)
        # mat[row][i] = sum of mat[row][0..i]
        for row in range(m):
            for i in range(1, n):
                self.mat[row][i] = self.mat[row][i - 1] + self.mat[row][i]
        
        # Pass 2: Col-wise prefix sum (applied to already row-prefix-summed matrix)
        # mat[i][col] = sum of entire rectangle from (0,0) to (i, col)
        for col in range(n):
            for i in range(1, m):
                self.mat[i][col] = self.mat[i-1][col] + self.mat[i][col]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Full rectangle sum from (0,0) to (row2, col2)
        total = self.mat[row2][col2]

        # Rectangle to the left of target region — from (0,0) to (row2, col1-1)
        left_region = self.mat[row2][col1 - 1] if col1 != 0 else 0

        # Rectangle above the target region — from (0,0) to (row1-1, col2)
        top_region = self.mat[row1 - 1][col2] if row1 != 0 else 0

        # Top-left corner overlap — subtracted twice above, so add back once
        # Rectangle from (0,0) to (row1-1, col1-1)
        intersection = self.mat[row1 - 1][col1 - 1] if (row1 != 0 and col1 != 0) else 0

        # Inclusion - Exclusion
        return total - (left_region + top_region) + intersection
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)




# ----------------------------------  Single Loop ------------------ ------------------- ------------------ -

#
# TC: O(m*n) precomputation, O(1) per query
# SC: O(1) extra space (modifies matrix in-place)
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix

        m = len(self.mat)
        n = len(self.mat[0])

        for row in range(m):
            for col in range(n):
                left = self.mat[row][col-1] if col > 0 else 0
                top  = self.mat[row-1][col] if row > 0 else 0
                intersection = self.mat[row-1][col-1] if (row > 0 and col > 0) else 0

                self.mat[row][col] = self.mat[row][col] + left + top - intersection

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Full rectangle sum from (0,0) to (row2, col2)
        total = self.mat[row2][col2]

        # Rectangle to the left of target region — from (0,0) to (row2, col1-1)
        left_region = self.mat[row2][col1 - 1] if col1 > 0 else 0

        # Rectangle above the target region — from (0,0) to (row1-1, col2)
        top_region = self.mat[row1 - 1][col2] if row1 > 0 else 0

        # Top-left corner overlap — subtracted twice above, so add back once
        # Rectangle from (0,0) to (row1-1, col1-1)
        intersection = self.mat[row1 - 1][col1 - 1] if (row1 > 0 and col1 > 0) else 0

        # Inclusion - Exclusion
        return total - (left_region + top_region) + intersection
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# ---------------------------------- Same Single Loop ------------------ ------------------- ------------------ -
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])

        self.matrix = matrix

        for i in range(m):
            for j in range(n):
                # First cell
                if i == 0 and j == 0:
                    continue
                
                # First row
                if i == 0:
                    self.matrix[i][j] = self.matrix[i][j-1] + self.matrix[i][j]
                
                # First col
                elif j == 0:
                    self.matrix[i][j] = self.matrix[i-1][j] + self.matrix[i][j]
                
                else:
                    self.matrix[i][j] = self.matrix[i][j] + ((self.matrix[i-1][j] + self.matrix[i][j-1]) - self.matrix[i-1][j-1])
        


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        sum_of_ele = self.matrix[row2][col2] 
        
        left_region = self.matrix[row2][col1 - 1] if col1-1 >=0 else 0
        
        upper_region = self.matrix[row1 - 1][col2] if row1-1 >= 0 else 0 

        diagonal = self.matrix[row1 - 1][col1 - 1] if (row1-1 >=0 and col1-1 >= 0) else 0
        
        return sum_of_ele - (left_region + upper_region) + diagonal
        