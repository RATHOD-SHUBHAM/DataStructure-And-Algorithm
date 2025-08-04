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

# Tc: O(m x n)
# Sc: O(m + n)

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

# Tc: O(m x n)
# Sc: O(1)

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