# TC: log(n!)
# sc: O(1)

class Solution:
    def binarySearch(self, matrix, target, start, col_search):
        left = start
        right = len(matrix[0]) - 1 if col_search else len(matrix) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if col_search:
                if target < matrix[start][mid]:
                    right = mid - 1
                elif target > matrix[start][mid]:
                    left = mid + 1
                else:
                    return True
            else:
                if target < matrix[mid][start]:
                    right = mid - 1
                elif target > matrix[mid][start]:
                    left = mid + 1
                else:
                    return True
                
        return False
                
            
    
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        
        if m == 0:
            return False
        
        n = len(matrix[0])
        
        # move inwards
        for i in range(min(m , n)):
            # find in col
            found_in_col = self.binarySearch(matrix, target, i, True)
            
            # find in row
            found_in_row = self.binarySearch(matrix, target, i, False)
            
            # if found somewhere
            if found_in_row or found_in_col:
                return True
            
        return False