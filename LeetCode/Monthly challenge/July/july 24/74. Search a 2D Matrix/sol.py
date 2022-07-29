# Tc: O(log(mn)), where m and n is the size of matrix
# Sc: O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        
        if m == 0:
            return False
        
        n = len(matrix[0])
        
        left = 0
        right = m * n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            mid_ele = matrix[mid // n][mid % n]
            
            if target == mid_ele:
                return True
            elif target < mid_ele:
                right = mid - 1
            else:
                left = mid + 1
                
        return False