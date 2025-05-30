class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        cellZero = False # Extra row cel for the 0th column

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

        # mark the first row with zero if zero is present
        if matrix[0][0] == 0:
            for i in range(m):
                matrix[i][0] = 0
        
        # mark the first column with zero
        if cellZero == True:
            for j in range(n):
                matrix[0][j] = 0
        
        return matrix