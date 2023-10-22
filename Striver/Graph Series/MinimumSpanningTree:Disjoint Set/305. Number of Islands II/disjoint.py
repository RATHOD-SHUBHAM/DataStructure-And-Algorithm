'''
    Classic Dynamic graph problem, Also known as online query.

    Dynamic Graph:
        Graph can change at any time.

    How in this question:
        We may perform an add land operation which turns the water at position into a land.
        This mean, add land operation can be performed anytime. 
        When this is performed a new land is added to graph.
'''


class Disjoint:
    def __init__(self, n):
        self.rank = [1] * (n + 1)
        self.parent = [i for i in range(n)]
        
    def findParent(self, x):
        if self.parent[x] != x:
            # path compression
            self.parent[x] = self.findParent(self.parent[x])
        
        return self.parent[x]
    
    def union_rank(self, u, v):
        # step 1: Find the ultimate parent
        pu = self.findParent(u)
        pv = self.findParent(v)
        
        # if they belong to same connected component
        if pv == pu:
            return
        
        # step 2: Get rank of parent
        rank_pv = self.rank[pv]
        rank_pu = self.rank[pu]
        
        # step 3: attach smaller rank to larger rank
        if rank_pu < rank_pv:
            self.parent[pu] = pv
        elif rank_pv < rank_pu:
            self.parent[pv] = pu
        else:
            self.parent[pu] = pv
            self.rank[pv] += 1


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        V = (m * n) # no of nodes
        disjoin_obj = Disjoint(V)
        
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        no_of_island = 0
        
        answer = [] # store the no of island dynamically
        
        for pos in positions:
            u , v = pos
            
            # there might be repeated cell
            if visited[u][v] == True:
                # at present how many island are present - store that
                answer.append(no_of_island)
                continue
                
            no_of_island += 1 # he himself is a island initially
            
            visited[u][v] = True
            
            # explore the neighbors
            for direction in directions:
                adj_row , adj_col = direction
                
                nei_u = u + adj_row
                nei_v = v + adj_col
                
                # visited will keep track of adjacent land at that point in time.
                if nei_u < 0 or nei_v < 0 or nei_u >= m or nei_v >= n or visited[nei_u][nei_v] == False:
                    continue
                
                # get the cell number -- (i * n + j)
                node = u * n + v
                nei_node = nei_u * n + nei_v
                
                # check if they have the same ultimate parent 
                p_node = disjoin_obj.findParent(node)
                p_nei = disjoin_obj.findParent(nei_node)
                
                if p_node != p_nei:
                    no_of_island -= 1
                    # create a union since they are neighbors
                    disjoin_obj.union_rank(node , nei_node)
            
            # after exploring all the neighbor - add the island to answer.
            answer.append(no_of_island)
            
        return answer