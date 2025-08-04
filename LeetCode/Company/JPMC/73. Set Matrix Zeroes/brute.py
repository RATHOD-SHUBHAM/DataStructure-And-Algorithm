# ----------------------------- Using List -----------------------------
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        # Grab the cell where there is 0
        col = [0] * n
        row = [0] * m

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    col[j] = 1
                    row[i] = 1
        

        # Make the row = 0
        for i in range(m):
            if row[i] == 0:
                continue
            for j in range(n):
                matrix[i][j] = 0
        
        # Make the col 0
        for j in range(n):
            if col[j] == 0:
                continue
            for i in range(m):
                matrix[i][j] = 0
        
        return matrix
    
# ----------------------------- Using Set -----------------------------

# Tc: O(m x n)
# Sc: O(m + n)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        # Grab the cell where there is 0
        col_set = set()
        row_set = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    col_set.add(j)
                    row_set.add(i)
        

        # Make the row and col 0
        for i in row_set:
            for j in range(n):
                matrix[i][j] = 0
        
        for j in col_set:
            for i in range(m):
                matrix[i][j] = 0
        
        return matrix
    

