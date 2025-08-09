# Dynamic graph
class Disjoint:
    def __init__(self, n):
        self.size = [0] * (n + 1)
        self.parent = [i for i in range(n + 1)]
    
    def findParent(self, x):
        if self.parent[x] != x:
            # path comprehension
            self.parent[x] = self.findParent(self.parent[x])
        
        return self.parent[x]
    
    def union_size(self, u, v):
        # step 1: find the ultimate parent of u and v
        pu = self.findParent(u)
        pv = self.findParent(v)

        if pu == pv:
            return

        # step 2: Find the sise of ultimate parent
        size_pu = self.size[pu]
        size_pv = self.size[pv]

        # step 3: attach smaller size to larger size parent
        if size_pu < size_pv:
            self.parent[pu] = pv
        elif size_pv < size_pu:
            self.parent[pv] = pu
        else:
            self.parent[pu] = pv
            self.size[pv] += 1

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # cell position: u * n + v
        V = m * n
        disjoint_obj = Disjoint(V)

        answer = []

        no_of_island = 0

        visited = [False] * V # this will keep track of land cell

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for u, v in positions:
            cur_cell_no = u * n + v

            # Check if the current cell is already land
            if visited[cur_cell_no] == True:
                answer.append(no_of_island)
                continue

            no_of_island += 1
            visited[cur_cell_no] = True

            for adj_row, adj_col in directions:
                nei_u = adj_row + u
                nei_v = adj_col + v

                nei_cell_no = nei_u * n + nei_v

                # Check if the neighbor cell is within bounds and 
                # Check if there is land
                if nei_u < 0 or nei_u >= m or nei_v < 0 or nei_v >= n or visited[nei_cell_no] == False:
                    continue
                
                # If there is a land cell and it is not already connected
                # to the current cell, then we can union them
                if disjoint_obj.findParent(cur_cell_no) != disjoint_obj.findParent(nei_cell_no):
                    disjoint_obj.union_size(cur_cell_no, nei_cell_no)
                    no_of_island -= 1

            answer.append(no_of_island)
        
        return answer
    
# ----------------------------- Union By Rank
class Disjoint:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n)]
    
    def findParent(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.findParent(self.parent[x])

        return self.parent[x]
    
    def find_union(self, u, v):
        # Step 1: Find the ultimate parent
        pu = self.findParent(u)
        pv = self.findParent(v)

        if pu == pv:
            return

        # Step 2: Get the rank of ultimate parent
        rank_pu = self.rank[pu]
        rank_pv = self.rank[pv]

        # Step 3: Merge smaller rank to larger ones
        if rank_pu < rank_pv:
            self.parent[pu] = pv
        elif rank_pv < rank_pu:
            self.parent[pv] = pu
        else:
            self.parent[pu] = pv
            self.rank[pv] += 1

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        V = m * n # Total No of cell

        disjoint_obj = Disjoint(V)

        # Keep track of the Land cell -> True = Land
        visited = [False] * V

        op = []
        no_of_island = 0

        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for u, v in positions:
            cell_no = u * n + v

            # check if this cell is already a land
            if visited[cell_no] == True:
                op.append(no_of_island)
                continue
            
            # Convert to land
            visited[cell_no] = True

            no_of_island += 1

            for nei in neighbors:
                nei_u = nei[0] + u
                nei_v = nei[1] + v

                nei_cell_no = nei_u * n + nei_v

                # if the neigbor is inbound and is a land
                if nei_u < 0 or nei_u >= m or nei_v < 0 or nei_v >= n or visited[nei_cell_no] == False:
                    continue
                
                # check if union can be formed
                if disjoint_obj.findParent(cell_no) != disjoint_obj.findParent(nei_cell_no):
                    disjoint_obj.find_union(cell_no, nei_cell_no)
                    no_of_island -= 1

            
            op.append(no_of_island)
        
        return op