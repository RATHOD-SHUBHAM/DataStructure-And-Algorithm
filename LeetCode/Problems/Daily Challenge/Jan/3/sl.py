# Tc: O(m *n) | Sc: O(1)
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        no_of_col = 0
        
        row_len = len(strs)
        col_len = len(strs[0])
        
        # loop through each ele like that of a matrix
        for col in range(col_len):
            for row in range(1, row_len):
                
                # check if the elements are not sorted
                if ord(strs[row - 1][col]) >= ord(strs[row][col]):
                    no_of_col += 1
                    break
                    
        return no_of_col