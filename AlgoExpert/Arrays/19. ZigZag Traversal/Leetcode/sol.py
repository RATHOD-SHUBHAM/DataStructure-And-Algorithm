'''
Logic is: When Even we hit a border we move Up or Down.

When we are row == 0 or col == last col. We want to move down.
When we are at col == 0 or row == last row. We want to move up

'''
# Time = O(row.col) 
# Space = O(1). If we dont consider op.
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = 0
        col = 0
        height = len(mat) - 1
        width = len(mat[0]) - 1
        
        res = []
        
        goingUp = True
        
        while not self.isBound(row, col, height, width):
            
            res.append(mat[row][col])
            
            if goingUp:

                if row == 0 or col == width:
                    goingUp = False # go Down
                    
                    if col == width:
                        row += 1
                    else:
                        col += 1
                        
                else:
                    row -= 1
                    col += 1
            
            else:
                if col == 0 or row == height:
                    goingUp = True
                    
                    if row == height:
                        col += 1
                    else :
                        row += 1
                        
                else:
                    row += 1
                    col -= 1   
        
        return res
    
    def isBound(self, row, col, height, width):
        # this will return true if any of this condition is met
        return row < 0 or col < 0 or row > height or col > width