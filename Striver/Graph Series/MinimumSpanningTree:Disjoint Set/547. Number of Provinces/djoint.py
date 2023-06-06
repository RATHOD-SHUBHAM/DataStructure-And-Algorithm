# Tc: O(n^2) | Sc: O(n)

class Disjoint:
    # Sc: O(n)
    def __init__ (self, n):
        self.rank = [1] * (n + 1)
        self.parent = [i for i in range(n)]
        
    
    def findParent(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.findParent(self.parent[x])
            
        return self.parent[x]
    
    def union_rank(self, u, v):
        # step 1: Find ultimate parent of u and v
        pu = self.findParent(u)
        pv = self.findParent(v)
        
        # check if they are in the same component
        if pu == pv:
            return
        
        # step 2: get the rank of ultimate parent
        rank_pu = self.rank[pu]
        rank_pv = self.rank[pv]
        
        # step 3: Attach the smaller rank to larger on
        if rank_pu < rank_pv:
            self.parent[pu] = pv
        elif rank_pv < rank_pu:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
    
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        disjoint_obj = Disjoint(n)
        
        # Tc: O(n^2)
        for u in range(n):
            for v in range(n):
                # if there is an edge then connect the component
                if isConnected[u][v] == 1:
                    disjoint_obj.union_rank(u ,v)
        
        # Tc: O(n)
        no_of_province = 0
        # the unique parent are the total no of province
        for i in range(n):
            if disjoint_obj.findParent(i) == i:
                no_of_province += 1
        
        return no_of_province