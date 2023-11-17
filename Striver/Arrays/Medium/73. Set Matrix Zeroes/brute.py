class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        # Get the row and column where there is zero
        row_col = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_col.add((i,j))
        
        # mark all the row col with 0
        for row, col in row_col:


            for j in range(n):
                if matrix[row][j] != 0:
                    matrix[row][j] = 0



            for i in range(m):
                if matrix[i][col] != 0:
                    matrix[i][col] = 0

    
        
        return matrix