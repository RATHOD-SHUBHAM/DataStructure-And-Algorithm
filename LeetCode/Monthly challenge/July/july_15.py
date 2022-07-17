'''

695. Max Area of Island

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.

'''

# Tc: (m * n)
# Sc: (1)

from typing import List

class Solution:
    def dfs(self, grid, row, col):
        grid[row][col] = 0 # mark as visited
        
        area_of_island = 1 # current island
        
        four_direction = [(row - 1, col), (row + 1, col) , (row , col - 1), (row , col + 1)]
        
        for cur_row, cur_col in four_direction:
            if 0 <= cur_row < len(grid) and 0 <= cur_col < len(grid[0]) and grid[cur_row][cur_col] == 1:
                area_of_island += self.dfs(grid, cur_row, cur_col)
                
        return area_of_island
        
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area_of_island = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area_of_island = max(area_of_island , self.dfs(grid, row, col))
        
        return area_of_island


if __name__ == '__main__':
    sol = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(sol.maxAreaOfIsland(grid))
    grid = [[0,0,0,0,0,0,0,0]]
    print(sol.maxAreaOfIsland(grid))
