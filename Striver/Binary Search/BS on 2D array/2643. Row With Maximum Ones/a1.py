# -------------------------------- Binary Search --------------------------------

class Solution:
    def getOnesCount(self, arr, n):
        arr.sort()

        left = 0
        right = n - 1

        ones_start_idx = -1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == 1:
                ones_start_idx = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ones_start_idx if ones_start_idx == -1 else n - ones_start_idx




    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        max_ones = 0
        max_idx_row = 0

        for row in range(m):
            # Count no of ones
            ones_count = self.getOnesCount(mat[row], n)

            if ones_count > max_ones:
                max_ones = ones_count
                max_idx_row = row
        
        return [max_idx_row, max_ones]


# -------------------------------- Inbuilt Func --------------------------------

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        max_ones = 0
        max_idx_row = 0

        for idx in range(m):
            row = mat[idx]
            
            # Count no of ones
            ones_count = row.count(1)

            if ones_count > max_ones:
                max_ones = ones_count
                max_idx_row = idx
        
        return [max_idx_row, max_ones] 
