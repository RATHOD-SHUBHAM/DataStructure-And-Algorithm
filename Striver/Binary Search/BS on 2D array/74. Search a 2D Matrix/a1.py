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
    
# -------------------------- 1D to 2D --------------------------

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        V = m * n

        left = 0
        right = V - 1

        while left <= right:
            mid = left + (right - left) // 2

            # Convert to 2D coordinates
            row = mid // n
            col = mid % n

            cur_ele = matrix[row][col]

            if cur_ele == target:
                return True
            elif cur_ele < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False