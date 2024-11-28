class Solution:
    def rowWithMax1s(self, arr):
        # code here
        m = len(arr)
        n = len(arr[0])
        
        for col in range(n):
            for row in range(m):
                if arr[row][col] == 1:
                    return row
        
        return -1
    

# -------------------- Count --------------------
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