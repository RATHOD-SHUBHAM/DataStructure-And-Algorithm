from collections import defaultdict
class Disjoint:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n+1)]
    
    def findParent(self, x):
        if self.parent[x] != x:
            # path comprehension
            self.parent[x] = self.findParent(self.parent[x])
        return self.parent[x]
    
    def union_rank(self, u , v):
        # Step 1: find the ultimate parent of u ,v
        pu = self.findParent(u)
        pv = self.findParent(v)

        if pu == pv:
            return
        
        # Step 2: get the rank of ultimate parent
        rank_pu = self.rank[pu]
        rank_pv = self.rank[pv]

        # Step 3: Attach smaller rank parent to higher rank
        if rank_pu < rank_pv:
            self.parent[pu] = pv
        elif rank_pv < rank_pu:
            self.parent[pv] = pu
        else:
            self.parent[pu] = pv
            self.rank[pv] += 1

class Solution:
    def buildGraph(self, dislikes):
        graph = defaultdict(list)

        for i in dislikes:
            u ,v = i
            graph[u].append(v)
            graph[v].append(u)
        
        return graph

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        disjoint_obj = Disjoint(n)

        graph = self.buildGraph(dislikes)
        print(graph)


        for i in range(1, n + 1):
            for nei in graph[i]:
                if disjoint_obj.findParent(i) == disjoint_obj.findParent(nei):
                    return False
                
                # create union between the neighbors
                disjoint_obj.union_rank(graph[i][0] , nei)
                
        return True