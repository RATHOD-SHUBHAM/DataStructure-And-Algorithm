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

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        island_size = -math.inf
        
        # Step 1: Group the islands together.
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
                    
                    # if they dont have common parent - merge the cells to form a common island
                    pu = disjoint_obj.findParent(node_cell)
                    pv = disjoint_obj.findParent(nei_cell)
                    
                    if pu != pv:
                        disjoint_obj.union_find(node_cell , nei_cell)

        # Step 2: convert non island cell to island and get the size
        
        for i in range(n):
            for j in range(n):
                
                if grid[i][j] == 1:
                    continue
                
                # grab the adjacent island for the current cell
                neighbouring_island = set()

                for direction in directions:
                    adj_row, adj_col = direction

                    nei_row = u + adj_row
                    nei_col = v + adj_col

                    if nei_row < 0 or nei_row >= n or nei_col < 0 or nei_col >= n or grid[nei_row][nei_col] == 0:
                        continue
                    
                    # grab the cell numbers
                    nei_node = nei_row * n + nei_col

                    parent_island = disjoint_obj.findParent(nei_node)

                    neighbouring_island.add(parent_island)
                # print(neighbouring_island)
                
                
                # step 3: Get the size of all the neighbouring_island of current cell
                current_island_size = 1
                for parent_island in neighbouring_island:
                    parent_island_size = disjoint_obj.size[parent_island]
                    current_island_size += parent_island_size

                island_size = max(island_size, current_island_size)

        
        # print(island_size)
        
        # if every node is a island
        ultimate_parent = disjoint_obj.findParent(0) # get ultimate parent of any node
        size_ultimate_parent = disjoint_obj.size[ultimate_parent]
        
        island_size = max(island_size, size_ultimate_parent)

        return island_size