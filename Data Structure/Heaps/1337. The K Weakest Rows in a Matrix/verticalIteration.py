'''
Rather than iterating row Wise. Iterate column wise.
Edge case:
    * If at a point my weakest row list is not same as k value. Then add the value row with 1


1* Iterate column wise --> for every row.
    * Check if there is a zero in col 0
    * For other col check if the previous col was 1
    
2* Check the edge case: 
    Eg [[1,0],[1,0],[1,0],[1,1]]
    4
    Add the row with all ones just to match the K value
    
    
# Time = O(m * n) space
# Space = O(1) if op array is not considered else O(n)
'''
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        weakest_row = []
        
        # Step 1
        for col in range(len(mat[0])):
            for row in range(len(mat)):
                # if we reach k value break
                if len(weakest_row) == k:
                    break
                
                # check for 0 is col 0
                if col == 0 and mat[row][col] == 0:
                    weakest_row.append(row)
                    
                # check for 0 where previous col had 1
                elif col != 0 and mat[row][col] == 0 and mat[row][col-1] == 1:
                    weakest_row.append(row)
                    
        # print(weakest_row)
        
        # step 2:
        row = 0
        while len(weakest_row) < k:
            if mat[row][-1] == 1:
                weakest_row.append(row)
            
            row += 1
                
        return weakest_row