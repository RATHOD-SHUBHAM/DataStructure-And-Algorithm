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