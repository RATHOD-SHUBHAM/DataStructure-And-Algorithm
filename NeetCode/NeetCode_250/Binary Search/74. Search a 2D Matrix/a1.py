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



# =============================================== Search 2D Matrix  ===============================================

# Tc: O(log(m*n)) | Sc: O(1)
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        # Flatten the index
        left = 0
        right = (m*n) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # Bring index back to 2D Space
            r = mid // n
            c = mid % n

            val = matrix[r][c]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
