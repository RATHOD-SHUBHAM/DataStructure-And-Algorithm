# Tc and Sc: O(n)
class Disjointset:
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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        disjoint_obj = Disjointset(n)
        
        # Count extra edge and create disjoint set
        extra_edge = 0
        c_len = len(connections)
        
        for i in range(c_len):
            u , v = connections[i]
            
            if disjoint_obj.findParent(u) == disjoint_obj.findParent(v):
                extra_edge += 1
            else:
                disjoint_obj.union_rank(u,v)
                
        # find the no of connected component
        no_of_province = 0
        for i in range(n):
            if disjoint_obj.findParent(i) == i:
                no_of_province += 1
                
        # to make an entire graph with N component connected we need N-1 edges
        # if we have 2 unique connected component we need 1 edge to coonect btn them
        no_of_edge = no_of_province - 1 # total no of edge required to make the graph connected
        if extra_edge >= no_of_edge:
            return no_of_edge
        else:
            return -1