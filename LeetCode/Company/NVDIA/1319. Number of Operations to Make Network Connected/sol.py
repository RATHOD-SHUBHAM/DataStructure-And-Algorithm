class Disjoint:
    def __init__(self, n):
        self.rank = [1] * (n +1)
        self.parent = [i for i in range(n)]
    
    def findParent(self, x):
        if self.parent[x] != x:
            # Path comprehension
            self.parent[x] = self.findParent(self.parent[x])
        
        return self.parent[x]
    
    def union_rank(self, u, v):
        # step 1: Find the ultimate parent
        pu = self.findParent(u)
        pv = self.findParent(v)

        if pu == pv:
            return

        # Step 2: grab the rank of ultimate parent
        rank_u = self.rank[pu]
        rank_v = self.rank[pv]

        # Step 3: attach smaller rank parent to larger rank
        if rank_u < rank_v:
            self.parent[pu] = pv
        elif rank_v < rank_u:
            self.parent[pv] = pu
        else:
            self.parent[pu] = pv
            self.rank[pv] += 1



class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        disjoint_obj = Disjoint(n)

        # Grab the extra connections
        extra_connection = 0
        for i in range(len(connections)):
            u , v = connections[i]

            if disjoint_obj.findParent(u) == disjoint_obj.findParent(v):
                extra_connection += 1
            else:
                disjoint_obj.union_rank(u,v)
            
        # no of province
        no_of_province = 0
        for i in range(n):
            if disjoint_obj.findParent(i) == i:
                no_of_province += 1
        
        # get the no of edges to connect all province together
        no_of_edge = no_of_province - 1

        if extra_connection >= no_of_edge:
             # Return minimum connection
            return no_of_edge
        else:
            return -1