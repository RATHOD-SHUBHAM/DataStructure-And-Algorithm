import collections

class Solution:
    def isCycle(self, V, edges):
        # Build Adj List
        graph = collections.defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            
        # Step 1: Get the indegree of the nodes
        indegree = [0] * V
        for u, v in edges:
            indegree[v] += 1
        
        # Step 2: Get all the nodes with no preq
        queue = collections.deque()
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
        
        # Iterate over the neighbors and unlock them
        count = 0
        topo_sort = []
        
        while queue:
            node = queue.popleft()
            
            for nei in graph[node]:
                indegree[nei] -= 1
                
                if indegree[nei] == 0:
                    queue.append(nei)
            
            count += 1
            topo_sort.append(node)
        
        if count == V:
            return False # No Cycle found
        else:
            return True # Cycle Found