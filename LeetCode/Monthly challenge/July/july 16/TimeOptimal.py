# TC, SC: O(mnN)
# Here, mm, nn refer to the number of rows and columns of the given grid respectively. NN refers to the total number of allowed moves.

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = (10 ** 9) + 7
        
        @lru_cache(None)
        def no_of_path(maxMove, row, col):
            
            # if reached boundary
            if row < 0 or row == m or col < 0 or col == n:
                return 1
            
            # Check of moves are over
            if maxMove == 0:
                return 0
            
            # decrement max move
            maxMove -= 1
            
            # move in 4 directions
            move = ( 
                no_of_path(maxMove, row - 1, col) +
                no_of_path(maxMove, row + 1, col) +
                no_of_path(maxMove, row, col - 1) +
                no_of_path(maxMove, row, col + 1) 
            ) % MOD
            
            return move

        
        
        return no_of_path(maxMove, startRow, startColumn)
        