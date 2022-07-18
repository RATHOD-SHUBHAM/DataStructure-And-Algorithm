class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = (10 ** 9) + 7
        count = 0
        
        dp = [[0] * n for _ in range(m)]
        
        ## marking the start position as 1. So that we can know the next moves
        dp[startRow][startColumn] = 1 
        
        # keep track of moves
        
        for _ in range(maxMove):
            
            # crete a temp each time i change my move
            temp_dp = [[0] * n for _ in range(m)]
            
            for row in range(m):
                for col in range(n):
                    # for the current grid check if i can move in 4 direction
                    for nr , nc in [(row - 1, col) , (row + 1, col) , (row , col - 1) , (row , col + 1)]:
                        if 0 <= nr < m and 0 <= nc < n:
                            # check if i can reach the cell from start row and start col
                            temp_dp[nr][nc] = (temp_dp[nr][nc] + dp[row][col]) % MOD
                        # if i move outside grid
                        else:
                            count = (count + dp[row][col]) % MOD
                        
                         
            # once i finished for start position
            # for next move copy the temp dp to main dp
            dp = temp_dp
            
        return count
                        
        
        