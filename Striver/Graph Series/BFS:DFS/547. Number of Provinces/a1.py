# Number of Province or Connected Component:

# ----------------------------------- BFS -------------------------------------------

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        visited = [False] * n

        queue = []

        no_of_province = 0

        for i in range(n):
            if visited[i] == True:
                continue
            
            queue.append(i)

            while queue:
                node = queue.pop(0)
                visited[node] = True

                for nei in range(len(isConnected[node])):
                    if isConnected[node][nei] == 0:
                        continue
                    
                    if visited[nei] == True:
                        continue
                    
                    queue.append(nei)
            
            no_of_province += 1
        
        return no_of_province

# -------------------------------------DFS-------------------------------------------

# Single Loop

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        visited = [False] * n

        # Helper -----------------------------------------------

        def dfs(i):

            if visited[i] == True:
                return
            
            visited[i] = True
            
            for j in range(n):
                
                if isConnected[i][j] == 1:
                    dfs(j)

            return


        # Main Function -------------------------------------------------
        
        count = 0
        
        for i in range(n):

            if visited[i] == True:
                continue

            dfs(i)

            count += 1

        return count
    

# ------ Sol 2 ------------------------

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        visited = [False] * n

        no_of_province = 0

        def dfs(idx):
            
            visited[idx] = True

            for nei in range(len(isConnected[idx])):
                if isConnected[idx][nei] == 0:
                    continue
                
                if visited[nei] == True:
                    continue
                
                dfs(nei)
            
            return


        for i in range(n):
            if visited[i] == True:
                continue
            
            dfs(i)
            no_of_province += 1
        
        return no_of_province


# ------------------------------------- Disjoint ----------------------------------------

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
        