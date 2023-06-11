class Disjoint:
    def __init__(self, n):
        self.size = [1] * (n + 1)
        self.parent = [i for i in range(n)]
        
    def findParent(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.findParent(self.parent[x])
        
        return self.parent[x]
    
    def union_find(self, u, v):
        # step 1: get the ultimate parent
        pu = self.findParent(u)
        pv = self.findParent(v)
        
        if pu == pv:
            return
        
        # step 2: get the size of ultimate parent
        size_pu = self.size[pu]
        size_pv = self.size[pv]
        
        # step 3: Attach the smaller weight to larger one
        if size_pu < size_pv:
            self.parent[pu] = pv
            self.size[pv] += size_pu
        elif size_pv < size_pu:
            self.parent[pv] = pu
            self.size[pu] += size_pv
        else:
            self.parent[pv] = pu
            self.size[pu] += size_pv

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if n == 1:
            return grid[0][0]
        
        V = (n * n)
        disjoint_obj = Disjoint(V)
        
        start_cell = grid[0][0]
        end_cell = grid[n-1][n-1]
        print(end_cell)
        
        depth = []
        for i in range(n):
            for j in range(n):
                depth.append((i,j))
        depth.sort()
        # print(depth)

        positions = sorted(depth, key = lambda x : grid[x[0]][x[1]] ) # grid[i][j] -> i = x[0], j = x[1]
        print(positions)
        
        
        visited = [[False for _ in range(n)] for _ in range(n)]
        directions = [(-1, 0), (1, 0), (0,-1), (0,1)]
        
        for x in positions:
            i , j = x
                
            visited[i][j] = True

            for nei in directions:
                adj_row , adj_col = nei

                nei_row = adj_row + i
                nei_col = adj_col + j

                if nei_row < 0 or nei_col < 0 or nei_row >= n or nei_col >= n or visited[nei_row][nei_col] == False:
                    continue

                # get the column number
                cell_no = grid[i][j]
                nei_cell_no = grid[nei_row][nei_col]


                # get the ultimate parent
                pu = disjoint_obj.findParent(cell_no)
                pv = disjoint_obj.findParent(nei_cell_no)

                if pu != pv:
                    disjoint_obj.union_find(cell_no, nei_cell_no)

                if disjoint_obj.findParent(start_cell) == disjoint_obj.findParent(end_cell):
                    return cell_no