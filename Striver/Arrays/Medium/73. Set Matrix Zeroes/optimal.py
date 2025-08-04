class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        # Step 1: Mark the cell
        # Grab the cell where there is 0
        col_0 = 1

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if j != 0:
                        matrix[0][j] = 0 # First row
                        matrix[i][0] = 0 # First col
                    else:
                        col_0 = 0
                        matrix[i][0] = 0
        

        # Step 2: Mark the internal boundary
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        # print(matrix)

        # Step 3: Mark the boundary
        # 3.1: First row
        for j in reversed(range(n)):
            if matrix[0][j] == 0 or matrix[0][0] == 0:
                    matrix[0][j] = 0
            
        # print(matrix)
        
        # 3.2: First col
        for i in range(m):
            if matrix[i][0] == 0 or col_0 == 0:
                    matrix[i][0] = 0
        
        return matrix