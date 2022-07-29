# Tc: O(m + n)
# Sc: O(1)

# start from last row and col value and move left or right
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        if m == 0 or n == 0:
            return False
        
        row = m - 1
        col = 0
        
        while row >= 0 and col < n:
            if target < matrix[row][col] :
                row -= 1
            elif target > matrix[row][col]:
                col += 1
            else:
                return True
            
        return False
        
        