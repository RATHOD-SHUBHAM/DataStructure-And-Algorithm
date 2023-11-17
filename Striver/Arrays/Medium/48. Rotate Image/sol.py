class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
       
        # Store the value in matrix
        lst = []
        
        for i in range(m):
            for j in range(n):
                
                if len(lst) == j:
                    lst.append([])

                lst[j].append(matrix[i][j])
        # print(lst)
        
        # Push the value back in the matix
        for i in range(m):
            for j in range(n):
                cur_num = lst[i][(n-1) - j]
                matrix[i][j] = cur_num
        
        return matrix