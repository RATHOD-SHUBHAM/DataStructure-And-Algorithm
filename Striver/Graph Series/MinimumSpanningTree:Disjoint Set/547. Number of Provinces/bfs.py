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