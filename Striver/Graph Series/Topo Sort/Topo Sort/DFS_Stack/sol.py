import collections

class Solution:
    
    def topoSort(self, V, edges):
        # Build Graph
        graph = collections.defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
        
        # Traverse Graph
        topo_sort = []
        visited = [False] * V
        
        for i in range(V):
            if visited[i] == True:
                continue
        
            self.dfs(i, graph, visited, topo_sort)
        
        # Reverse the order and return
        return topo_sort[::-1]
    
    def dfs(self, node, graph, visited, topo_sort):
        if visited[node] == True:
            return
    
        # Mark the node as visited
        visited[node] = True
        
        # Visit all the neighbors
        for nei in graph[node]:
            self.dfs(nei, graph, visited, topo_sort)
        
        # All its dependant nodes has been visited
        topo_sort.append(node)
        
        return
        