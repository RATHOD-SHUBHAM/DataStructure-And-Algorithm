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
