# ------------------  Brute Force ----------------------------------

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

 
# ------------------  Visited ----------------------------------

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        visited = [[False for _ in range(n)] for _ in range(m)]

        def makeZero(i: int, j: int) -> None:

            # Make the entire row as 0
            for col in range(n):
                if matrix[i][col] == 0 or visited[i][col] == True:
                    continue

                matrix[i][col] = 0
                visited[i][col] = True
                
            
            # Make the entire col as 0
            for row in range(m):
                if matrix[row][j] == 0 or visited[row][j] == True:
                    continue

                matrix[row][j] = 0
                visited[row][j] = True
            
            return

        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0 or visited[i][j] == True:
                    continue
                
                makeZero(i , j)
        
        return matrix
    
# ------------------  Better ----------------------------------

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        row = set()
        col = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in row or j in col:
                    matrix[i][j] = 0
        
        return matrix

# ------------------  Optimal Solution ----------------------------------

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        # keep track of zero in every col of first row
        cellZero = False # Extra row cell for the 0th column

        # Mark the col and row where there is zero
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    
                    matrix[0][j] = 0 # Mark the column as zero
                    
                    # Mark the row as zero
                    if i == 0:
                        cellZero = True
                    else:
                        matrix[i][0] = 0
                    
        
        # except the first row and column - mark the remaing cell zero
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Fill the first columns all row with zero, if zero is present
        if matrix[0][0] == 0:
            for i in range(m):
                matrix[i][0] = 0
        
        # Fill the first rows all column with zero
        if cellZero == True:
            for j in range(n):
                matrix[0][j] = 0
        
        return matrix