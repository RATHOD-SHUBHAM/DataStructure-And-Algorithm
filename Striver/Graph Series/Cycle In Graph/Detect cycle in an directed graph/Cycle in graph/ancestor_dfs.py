import collections

class Solution:
    def isCycle(self, V, edges):
        visited = [False] * V
        ancestor = [False] * V
        
        # Build Adj List
        graph = collections.defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            
        
        for i in range(V):
            if visited[i] == True:
                continue
            
            cyclePresent = self.dfs(i, visited, ancestor, graph)
            
            if cyclePresent == True:
                return True
        
        return False
    
    def dfs(self, node, visited, ancestor, graph):
        # Mark the node as visited
        visited[node] = True
        # Make it as a ancestor for its neighbors
        ancestor[node] = True
        
        # Explore its neighbors
        for nei in graph[node]:
            if visited[nei] == False:
                # If nei is not visited , then explore
                cyclePresent = self.dfs(nei, visited, ancestor, graph)
            
                if cyclePresent == True:
                    return True
            else:
                if ancestor[nei] == True:
                    return True
        
        ancestor[node] = False
        return False