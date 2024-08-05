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