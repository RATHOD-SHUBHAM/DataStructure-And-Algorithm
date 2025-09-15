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