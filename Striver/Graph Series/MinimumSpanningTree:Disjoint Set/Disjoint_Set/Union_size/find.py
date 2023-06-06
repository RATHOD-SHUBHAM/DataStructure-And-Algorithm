class Solution:
    def __init__(self, n):
        self.size = [1] * (n + 1) # this takes care of 0 and 1 based graph
        self.parent = [i for i in range(n)]

    def findParent(self, x):
        if self.parent[x] != x:
            # path compression
            self.parent[x] = self.findParent(self.parent[x])

        return self.parent[x]
    
    def union_find(self, u, v):
        # step 1: find the ultimate parent
        pu = self.findParent(u)
        pv = self.findParent(v)

        # if they have the same parent , then they belong to same component
        if pu == pv:
            return
        
        # step 2: find size of ultimate parent
        size_pu = self.size[pu]
        size_pv = self.size[pv]

        # step 3: Attach the smaller size to larger size and update the size
        if size_pu < size_pv:
            self.parent[pu] = pv
            # since we are attaching pu to pv - increase the size of pv
            self.size[pv] += self.size[pu]
        elif size_pv < size_pu:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            # when they have the same size, Attach anyone and update size and parent
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]


if __name__ == '__main__':
    obj = Solution(5)
    
    obj.union_find(0, 2)
    obj.union_find(4, 2)
    obj.union_find(3, 1)

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