# DFS + Stack:

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


# ------------------------------------------------------------------------

# Khans Algorithm : Cycle detection

import collections

class Solution:
    
    def topoSort(self, V, edges):
        # Build Graph
        graph = collections.defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
        
        # Step 1: Get the indegree of the nodes
        indegree = [0] * V
        
        for u, v in edges:
            indegree[v] += 1
        
        # Step 2: Get all the nodes with no pre-req or indegree = 0
        queue = collections.deque()
        
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
        
        # step 3: Iterate over the neighbour and unlock them
        count = 0 # This is useful to check if there are cycles in the graph
        topo_sort = []
        
        while queue:
            node = queue.popleft()
            
            for nei in graph[node]:
                # Unlock nei
                indegree[nei] -= 1
                
                # Check if nei has no prereq left
                if indegree[nei] == 0:
                    queue.append(nei)
                
            
            count += 1
            topo_sort.append(node)
        
        return topo_sort