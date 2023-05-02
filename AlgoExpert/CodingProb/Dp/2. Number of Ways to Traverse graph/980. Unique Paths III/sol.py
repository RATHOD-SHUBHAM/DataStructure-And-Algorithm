# TC: O(3^n) | Sc: O(n)

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # Find the starting square and count the number of empty squares 
        # iterate through the grid to get relevant info
        start_idx = None  # to store starting point
        count_zeros = 0  # to count number of squares to walk over
        
        for i in range(m):
            for j in range(n):
                # empty square
                if grid[i][j] == 0 :
                    count_zeros += 1
                
                # starting square
                if not start_idx and grid[i][j] == 1:
                    start_idx = (i, j)
                    
        # print(start_idx)
        # print(count_zeros)
        
        # perform DFS + backtracking to find valid paths
        return self.backtrack(start_idx[0], start_idx[1], count_zeros, m, n, grid)
        
    def backtrack(self, i, j, count_zeros, m, n, grid):
        """
        Backtracking algo to find all valid paths from (i, j).
        :param i: Index of row (start) of coordinate.
        :param j: Index of column (start) of coordinate.
        :returns: Total number of valid paths from (i, j).
        """

        result = 0
        four_directions = (i-1, j), (i+1, j), (i, j-1), (i, j+1)
        
        for x, y in four_directions:
            # border check
            if 0 <= x < m and 0 <= y < n:

                if grid[x][y] == 0:
                    # traverse down this path
                    grid[x][y] = -1 # mark the cell
                    count_zeros -= 1 # and reduce the zero count
                    result += self.backtrack(x, y, count_zeros, m, n, grid)


                    # backtrack and reset
                    grid[x][y] = 0
                    count_zeros += 1

                elif grid[x][y] == 2:
                    # check if all squares have been walked over
                    if count_zeros == 0: 
                        result += 1

        return result
        
        
