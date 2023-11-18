class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        # Total cell
        V = m * n

        left = 0
        right = V - 1

        while left <= right:
            mid = left + (right - left) // 2

            # cell value
            cur_val = matrix[mid // n][mid % n]

            if cur_val == target:
                return True
            elif cur_val > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False