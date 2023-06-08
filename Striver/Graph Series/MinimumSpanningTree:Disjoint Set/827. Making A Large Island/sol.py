# Change cell dynamically

class Disjoint:
    def __init__(self, n):
        self.size = [1] * (n + 1)
        self.parent = [i for i in range(n)]
        
    def findParent(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.findParent(self.parent[x])
            
        return self.parent[x]
    
    def union_find(self, u, v):
        # step 1 : find ultimate parent of u
        pu = self.findParent(u)
        pv = self.findParent(v)
        
        # check if they belong to same component
        if pu == pv:
            return
        
        # step 2: get size of ultimate parent
        size_pu = self.size[pu]
        size_pv = self.size[pv]
        
        # step 3: attach smaller size to lareget size
        if size_pu < size_pv:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        elif size_pv < size_pu:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
            
            
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # total no of cells
        V = (n * n)
        disjoint_obj = Disjoint(V)
        
        # step 1: Find the no of island and their size
        
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        # go accross and create a union of island
        for u in range(n):
            for v in range(n):
                
                if grid[u][v] == 0:
                    continue
                
                for nie in directions:
                    adj_row , adj_col = nie
                    
                    nei_u = adj_row + u
                    nei_v = adj_col + v
                    
                    # check for edges
                    if nei_u < 0 or nei_v < 0 or nei_u >= n or nei_v >= n or grid[nei_u][nei_v] == 0:
                        continue
                    
                    # get the cell number
                    node_cell = u * n + v
                    nei_cell = nei_u * n + nei_v
                    
                    # get ultimate parent of the node
                    pu = disjoint_obj.findParent(node_cell)
                    pv = disjoint_obj.findParent(nei_cell)
                    
                    if pu != pv:
                        disjoint_obj.union_find(node_cell , nei_cell)

        # step 2: Update the cell one by one and check
        island_size = 0
        
        for i in range(n):
            for j in range(n):
                
                if grid[i][j] == 1:
                    continue
                
                # step 2.1: identify the island beside it
                island_around = set()
                for nei in directions:
                    adj_row , adj_col = nei
                    
                    nei_row = adj_row + i
                    nei_col = adj_col + j
                    
                    # check for edges
                    if nei_row < 0 or nei_col < 0 or nei_row >= n or nei_col >= n or grid[nei_row][nei_col] == 0:
                        continue
                        
                    # get the ultimate parent of the island
                    island_cell = nei_row * n + nei_col
                    
                    parent_island = disjoint_obj.findParent(island_cell)
                    
                    island_around.add(parent_island)
                    
                
                # print(island_around)
                
                
                # step 2.2 : attach itself to adjacent island and check the size
                cur_island_size = 1 # current size of island
                for parent_island in island_around:
                    size_of_parent_island = disjoint_obj.size[parent_island]
                    cur_island_size += size_of_parent_island
                    
                island_size = max(island_size , cur_island_size)
        
        # print(island_size)
        
        # if every cell is one - return the size of any nodes ultimate parent
        pu = disjoint_obj.findParent(0)
        size_pu = disjoint_obj.size[pu]
        island_size = max(island_size , size_pu)
        
        return island_size