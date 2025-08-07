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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        disjoint_obj = Disjoint(n)
        
        for edge in edges:
            u, v = edge
            
            disjoint_obj.union_rank(u , v)
        
        # find the unique component
        number_of_connected_components = 0
        for i in range(n):
            if disjoint_obj.findParent(i) == i:
                number_of_connected_components += 1
        
        return number_of_connected_components