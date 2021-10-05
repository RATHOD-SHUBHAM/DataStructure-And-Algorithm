# todo: Dynamic Programming


'''

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.


'''

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # DP
        m = len(mat)
        n = len(mat[0])
        res = [[float('inf')] * n for i in range(m)]
        # first pass
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                else:
                    # min of neighbors
                    if i > 0:
                        res[i][j] = min(res[i][j], res[i - 1][j] + 1)
                    if j > 0:
                        res[i][j] = min(res[i][j], res[i][j - 1] + 1)
                        
                        
        # second pass
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < m - 1:
                    res[i][j] = min(res[i][j], res[i + 1][j] + 1)
                if j < n - 1:
                    res[i][j] = min(res[i][j], res[i][j + 1] + 1)
                    
        return res