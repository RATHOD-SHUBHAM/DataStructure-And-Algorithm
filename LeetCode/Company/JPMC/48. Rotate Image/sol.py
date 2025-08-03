class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        # Reverse
        matrix.reverse()
        

        # Transpose
        for i in range(m):
            for j in range(i+1, n):
                if i == j:
                    continue
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]
        
        return matrix