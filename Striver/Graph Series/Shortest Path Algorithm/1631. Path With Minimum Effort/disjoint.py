'''
    Kruskals Algorithm

    We  build an edgeList 
    which consists of the absolute difference between every adjacent cell in the matrix. 
    
    We also sort the edge list in non-decreasing order of difference.


    Building an edgeList :
        If we look at up and left node for every cell - Then we will cover all 4 direction neighbor by the time we reach the end

    Since we access the edges in increasing order of difference, 
    and the current edge connected the source and destination cell, 
    we are sure that the current difference is the maximum absolute difference in our path with minimum efforts.
'''

class Disjoint:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n+1)]
    
    def findParent(self, x):
        if self.parent[x] != x:
            # Path comprehension
            self.parent[x] = self.findParent(self.parent[x])
        
        return self.parent[x]
    
    def union_rank(self, u, v):
        # step 1: Find the Ultimate parent
        pu = self.findParent(u)
        pv = self.findParent(v)

        # step 2: Get the rank of ultimate parent
        rank_pu = self.rank[pu]
        rank_pv = self.rank[pv]

        # step 3: Compare and join
        if rank_pu < rank_pv:
            self.parent[pu] = pv
        elif rank_pv < rank_pu:
            self.parent[pv] = pu
        else:
            self.parent[pu] = pv
            self.rank[pv] += 1



class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])

        if m == 1 and n == 1:
            return 0

        V = m * n
        disjoint_obj = Disjoint(V)

        edgeList = []

        # Building edge list
        for row in range(m):
            for col in range(n):
                cell_no = row * n + col

                # Look up
                if row > 0:
                    diff = abs(heights[row - 1][col] - heights[row][col])

                    nei_cell_no = (row - 1) * n + col

                    edgeList.append([diff, nei_cell_no, cell_no])
                
                # Look Left
                if col > 0:
                    diff = abs(heights[row][col - 1] - heights[row][col])

                    nei_cell_no = row * n + (col - 1)

                    edgeList.append([diff, nei_cell_no, cell_no])

        
        # maximum absolute difference in increasing order
        edgeList.sort(key = lambda x : x[0])
        print(edgeList)


        for diff , u, v in edgeList:
            disjoint_obj.union_rank(u,v)

            if disjoint_obj.findParent(0) == disjoint_obj.findParent(row * n + col):
                return diff
        
        return -1



