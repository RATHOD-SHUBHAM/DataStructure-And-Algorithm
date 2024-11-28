# -------------------------- Check Row By Row --------------------------

class Solution:
    def findTarget(self, arr, n, target):
        left = 0
        right = n - 1

        while left <= right: 
            mid = left + (right - left) // 2

            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if self.findTarget(matrix[i], n, target) == True:
                return True
        
        return False
    

# -------------------------- 2D Binary --------------------------


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