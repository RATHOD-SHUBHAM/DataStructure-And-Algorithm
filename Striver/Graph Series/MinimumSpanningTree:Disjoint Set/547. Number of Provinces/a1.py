class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        visited = [False] * n
        
        # Helper -------
        def dfs(i):
            
            if visited[i] == True:
                return
            
            visited[i] = True
            
            for j in range(n):
                if isConnected[i][j] == 1 and visited[j] == False:
                    dfs(j)
                    
            return
                    
        
        
        # Main --------
        
        province = 0
        
        for i in range(n):
            if visited[i] == False:
                dfs(i)
                province += 1
        
        return province
    
# --------------------------- Seperate Function ---------------------------
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        graph = collections.defaultdict(list)

        for i in range(n):
            for j in range(n):
                if i == j: 
                    continue
                
                if isConnected[i][j] == 1:
                    graph[i].append(j)
        
        # print(graph)

        # DFS
        visited = [False] * n
        count = 0
        for i in range(n):
            if visited[i] == True:
                continue
            
            self.dfs(i, visited, graph)
            count += 1
        
        return count
    
    def dfs(self, node, visited, graph):
        visited[node] = True

        if node not in graph:
            return
        
        for nei in graph[node]:
            if visited[nei] == True:
                continue
            
            self.dfs(nei, visited, graph)
        
        return

# --------------------------- BFS ---------------------------
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        graph = collections.defaultdict(list)

        for i in range(n):
            for j in range(n):
                if i == j: 
                    continue
                
                if isConnected[i][j] == 1:
                    graph[i].append(j)
        
        # print(graph)

        # DFS
        visited = [False] * n
        count = 0
        for i in range(n):
            if visited[i] == True:
                continue
            
            self.bfs(i, visited, graph)
            count += 1
        
        return count
    
    def bfs(self, node, visited, graph):
        visited[node] = True

        queue = collections.deque()
        queue.append(node)

        if node not in graph:
            return
        
        while queue:
            node = queue.popleft()

            for nei in graph[node]:
                if visited[nei] == True:
                    continue
                
                visited[nei] = True
                queue.append(nei)
        return
    
# --------------------------- Disjoint Set ---------------------------
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