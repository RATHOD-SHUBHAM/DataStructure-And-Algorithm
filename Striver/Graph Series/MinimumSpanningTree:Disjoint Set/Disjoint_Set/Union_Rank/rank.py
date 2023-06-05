class Solution:
    def __init__(self, n):
        # n: no of nodes
        self.rank = [0] * (n + 1) # this will take care of both zero and one based index graph
        self.parent = [i for i in range(n)]

    def findParent(self, x):
        # if parent is not itself
        if self.parent[x] != x:
            # perform path compression
            self.parent[x] = self.findParent(self.parent[x])
        
        return self.parent[x]
    
    def union_rank(self, u, v):
        # step 1: Find the ultimate parent of u , v
        pu = self.findParent(u)
        pv = self.findParent(v)

        # if the ultimate parent are same, then they belong to same component, so do nothing
        if pv == pu:
            return

        # step 2: get the rank of ultimate parent
        rank_pu = self.rank[pu]
        rank_pv = self.rank[pv]

        # step 3: Attach smaller rank parent to larger one
        if rank_pu < rank_pv:
            # update parent
            self.parent[pu] = pv
        elif rank_pv < rank_pu:
            self.parent[pv] = pu
        else:
            # when the rank are same . Update one as parent and increase rank
            self.parent[pv] = pu
            self.rank[pu] += 1


if __name__ == '__main__':
    obj = Solution(5)
    
    obj.union_rank(0, 2)
    obj.union_rank(4, 2)
    obj.union_rank(3, 1)

    # check if 4 and 0 are in the same connected component
    if obj.findParent(4) == obj.findParent(0):
        print('Yes')
    else:
        print('No')

    # check if 1 and 0 are in the same connected component
    if obj.findParent(1) == obj.findParent(0):
        print('Yes')
    else:
        print('No')