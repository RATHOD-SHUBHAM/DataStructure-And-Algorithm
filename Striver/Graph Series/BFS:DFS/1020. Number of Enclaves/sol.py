'''
    Clever Stratergy:
        1. So bascially if we dont hit the border, then we will have a count greater than zero.
        2. Instead of using visited array, we can convert 1 to 0.
'''
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        no_of_enclaves = 0
        for i in range(m):
            for j in range(n):

                if grid[i][j] == 0:
                    continue
                
                count = self.dfs(i, j, grid, m, n)

                # this trick will help us skip the borders
                if count > 0:
                    no_of_enclaves += count
        
        return no_of_enclaves

    def dfs(self, i, j, grid, m, n):
        # if we hit a border -> return a bizzar large negative number
        if i < 0 or j < 0 or i >= m or j >= n:
            return -math.inf
        
        if grid[i][j] == 0:
            return 0
        
        # mark the cell as visited
        grid[i][j] = 0

        up = self.dfs(i - 1, j, grid, m, n)
        down = self.dfs(i + 1, j, grid, m, n)
        left = self.dfs(i, j - 1, grid, m, n)
        right = self.dfs(i, j + 1, grid, m, n)

        return 1 + (up + down + left + right)

