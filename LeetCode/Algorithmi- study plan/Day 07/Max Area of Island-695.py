'''

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

'''
1. go through the grid
2. check for 1.
3. when there is 1 
    1. convert it to zero
    2. increase the area count by one
    3. check for adjusent cell if the have one or zero
    4 if 1 repeate step3
    
4. return max area

'''

class Solution:
    
    def dfs(self, grid, row, col):
        grid[row][col] = 0
        area_of_island = 1
        
        four_cells_around_current_cell = [(row - 1, col), (row + 1, col), (row , col + 1), (row, col - 1)]
        
        for row,col in four_cells_around_current_cell:
            print(row)
            print(col)
        
            if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == 1:
                area_of_island += self.dfs(grid, row, col)
                
        return area_of_island
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area_of_island = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area_of_island = max(area_of_island, self.dfs(grid,row,col))
                
        return area_of_island