# if suppose there are 6 nodes
# we compress them and check how many of them can be merged/removed
# after compressing lets assume that we have 2 nodes left that cant be merged
# this mean out of 6 nodes we cannot merge 2 nodes. that means 4 nodes can be merged.
# this 4 node is nothing but the nodes that can be removed
# No_of_stones_that_can_be_removed = Total_stones + Connected Component

import math
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

# perform coordinate mapping since this is a 2D grid.
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        total_no_of_stones = len(stones)
        
        # get the size of grid -------------------
        m = -math.inf
        n = -math.inf
        
        for row, col in stones:
            m = max( m , row)
            n = max(n , col)
        
        # print(m , n)
        
        # Coordinate Shift -------------------------
        V = (m + 1) + (n + 1) # total no of nodes -  2D grid
        
        disjoint_obj = Disjoint(V)
        
        for stone in stones:
            u , v = stone
            # Since this is a 2D grid, we perform coordinate shift on Column
            v = v + m + 1
            # print(u ,v)
            
            disjoint_obj.union_rank(u,v)
        
        # keep track of cell that has stone --------------
        stone_set = set()
        for row, col in stones:
            stone_set.add(row)
            
            col = col + m + 1
            stone_set.add(col)
        # print(stone_set)
        
        
        # Find no of unique province -------------------
        no_of_province = 0
        for i in range(V):
            if i in stone_set and disjoint_obj.findParent(i) == i:
                no_of_province += 1
        
        # print(no_of_province)
        
        return total_no_of_stones - no_of_province