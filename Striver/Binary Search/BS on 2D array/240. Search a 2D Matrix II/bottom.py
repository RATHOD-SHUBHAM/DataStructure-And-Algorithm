# the best way to start is from bottom left
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        
        if m == 0:
            return False
        
        n = len(matrix[0])
        
        row = m - 1
        col = 0
        
        while row >= 0 and col < n:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1
                
        return False
            