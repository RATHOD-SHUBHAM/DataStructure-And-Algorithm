# Time and Sc: O(N^2)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (self.isValidRow(board) and self.isValidCol(board) and self.isValidBlock(board))
    
    # check if the element are unique in the row
    def isValidRow(self, board):
        for row in board:
            # check if the current row is valid : has unique elements
            if not self.isValid(row):
                return False
        return True
    
    # check if the elements in the col are unique
    def isValidCol(self, board):  
        # zip(board) => row zip(*board): col
        for col in zip(*board):
            if not self.isValid(col):
                return False
        return True
    
    # check if the block has unique value
    def isValidBlock(self, board):
        # jump 3 cell each time
        for i in range(0,9,3):
            for j in range(0,9,3):
                '''val = []
                # cover with in 3 cell
                for x in range(i , i+3):
                    for y in range(j, j+3):
                        val.append(board[x][y])
                        '''
                val = [board[x][y] for x in range(i , i+3) for y in range(j , j+3)]
                
                if not self.isValid(val):
                    return False
                
        return True
    
                
        
    def isValid(self, arr):
        ele = [i for i in arr if i != "."]
        set_ele = set(ele)
        # check for duplicates
        return len(ele) == len(set_ele)
            