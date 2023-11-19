# Tc: O(m . n)
# Sc: O(1)

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row_len = len(mat)
        col_len = len(mat[0])
        
        index = []
        
        for col, row in itertools.product(range(col_len) , range(row_len)):
            
            if len(index) == k:
                break
                
            '''
            if the cur cell is 0
            check if this is the first col
            or check if the previous col had a 1 in it
            '''
            if mat[row][col] == 0 and (col == 0 or mat[row][col - 1] == 1):
                index.append(row)
                
        '''
        if there are all row with 1.
        check the last col to check there is a 1
        '''
        
        row = 0
        while len(index) < k:
            if mat[row][-1] == 1:
                index.append(row)
            row += 1
            
        return index