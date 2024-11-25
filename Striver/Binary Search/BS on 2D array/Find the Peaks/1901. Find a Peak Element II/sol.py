class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        left = 0
        right = m - 1

        while left <= right:
            row_idx = left + (right - left) // 2 # mid
            arr = mat[row_idx]
            
            max_ele = max(arr)
            col_idx = arr.index(max_ele)

            # Compare with the element above and below
            if (row_idx == 0 or mat[row_idx - 1][col_idx] < mat[row_idx][col_idx]) and (row_idx == m - 1 or mat[row_idx][col_idx] > mat[row_idx + 1][col_idx]) :
                return [row_idx, col_idx]
            elif row_idx - 1 >= 0 and mat[row_idx - 1][col_idx] > mat[row_idx][col_idx]:
                right = row_idx - 1
            elif row_idx + 1 < m and mat[row_idx + 1][col_idx] > mat[row_idx][col_idx]:
                left = row_idx + 1