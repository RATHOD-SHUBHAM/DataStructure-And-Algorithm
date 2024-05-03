#Tc : O(M Log M) | Sc: O(M)

class Disjoint:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n)]
        
    def findParent(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.findParent(self.parent[x])
            
        return self.parent[x]
        
    def union_rank(self, u, v):
        # step 1: get the ultimate parent of u and v
        pu = self.parent[u]
        pv = self.parent[v]
        
        # check if the belong to same component
        if pu == pv:
            return
        
        # step 2:  get rank of ultimate parent
        rank_pu = self.rank[pu]
        rank_pv = self.rank[pv]
        
        # step 3: attach smaller rank to larger one
        if rank_pu < rank_pv:
            self.parent[pu] = pv
        elif rank_pv < rank_pu:
            self.parent[pv] = pu
        else:
            # attach anyone to another and increase the rank
            self.parent[pv] = pu
            self.rank[pu] += 1
    
    
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        # step 1: Sort the weights
        # since this is adj list , we create a edges list of [weight , source , child]
        edges = []
        
        for i in range(V):
            for edge in adj[i]:
                v , wt = edge
                u = i
                
                edges.append((wt, u, v))
                
        # Step1 : Sorting the weights
        edges.sort(key = lambda x : x[0]) # this will help connecting the smaller weight first.
        
        # print(edges)
        
        # step 2: perform disjoin set operation
        # if they belong to same component add the edges to MST
        
        disjoint_obj = Disjoint(V) # disjoint set object
        
        MST_sum = 0
        MST = []
        
        for edge in edges:
            wt , u , v = edge
            
            # check it they dont belong to same Component
            if disjoint_obj.findParent(u) != disjoint_obj.findParent(v):
                MST_sum += wt
                MST.append((u, v))
                # connect the component
                disjoint_obj.union_rank(u ,v)
        
        return MST_sum