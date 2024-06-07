# -------- Transpose _ Reverse --------
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
       
        # Transpose
        for i in range(m):
            for j in range(i+1, n):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
        
        # print(matrix)
        
        # Reverse
        for i in range(m):
            matrix[i].reverse()

        return matrix



# -------- Reverse _ Transpose --------
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        matrix.reverse()

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(i, n):
                if i == j:
                    continue
                
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # print(matrix)
        return matrix
                

                
        