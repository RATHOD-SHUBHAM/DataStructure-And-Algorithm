class Disjoint:
    def __init__(self, n):
        self.rank = [0] * (n+1)
        self.parent = [i for i in range(n+1)]
    
    def findParent(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.findParent(self.parent[x])
        
        return self.parent[x]

    def union_rank(self, u ,v):
        pu = self.findParent(u)
        pv = self.findParent(v)

        if pu == pv:
            return

        rank_pu = self.rank[pu]
        rank_pv = self.rank[pv]

        if rank_pu < rank_pv:
            self.parent[pu] = pv
        elif rank_pv < rank_pu:
            self.parent[pv] = pu
        else:
            self.parent[pu] = pv
            self.rank[pv] += 1


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        disjoint_obj = Disjoint(n)

        for u in range(n):
            for v in range(n):
                if isConnected[u][v] == 1:
                    disjoint_obj.union_rank(u,v)

        
        untimate_parent = 0
        for i in range(n):
            if disjoint_obj.findParent(i) == i:
                untimate_parent += 1
        
        return untimate_parent
        