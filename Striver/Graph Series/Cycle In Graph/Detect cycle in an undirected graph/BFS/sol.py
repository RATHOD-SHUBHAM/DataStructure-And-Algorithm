import collections

class Solution:
    def isCycle(self, V, edges):
        graph = collections.defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * V
        
        for i in range(V):
            if visited[i] == True:
                continue
            
            parent = -1
            cyclePresent = self.bfs(i, parent, visited, graph)
            
            if cyclePresent == True:
                return True
        
        return False

    def bfs(self, i, parent, visited, graph):
        queue = collections.deque()
        queue.append((i, parent))
        
        visited[i] = True
        
        while queue:
            node, par = queue.popleft()
            
            for nei in graph[node]:
                if visited[nei] == True:
                    if nei == par:
                        continue
                    else:
                        return True
                else:
                    visited[nei] = True
                    queue.append((nei, node))
        
        return False
                    