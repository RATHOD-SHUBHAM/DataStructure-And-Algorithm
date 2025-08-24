#  ------ ------ Ancestor algorithm ------ ------ ------ ------

# TC: O(V + E) | SC : O(V)
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
                

#  ------ ------ Kahns algorithm ------ ------ ------ ------
# Tc: O(v+e) | Sc: O(n)

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