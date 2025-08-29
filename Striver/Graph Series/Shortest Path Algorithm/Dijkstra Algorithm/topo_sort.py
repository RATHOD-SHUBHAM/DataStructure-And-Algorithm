from typing import List
import collections
import math

class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        # Build Graph
        graph = collections.defaultdict(list)
        indegree = [0] * V
        for edge in edges:
            node, nei, wt = edge
            graph[node].append((nei, wt))
            indegree[nei] += 1
        
        queue = collections.deque()
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
        
        topo_sort = []
        while queue:
            node = queue.popleft()
            
            for neighbors in graph[node]:
                nei, wt = neighbors
                
                indegree[nei] -= 1
                
                if indegree[nei] == 0:
                    queue.append(nei)
            
            topo_sort.append(node)
        
        # Get distance
        dist = [math.inf] * V
        dist[0] = 0
        
        for node in topo_sort:
            if dist[node] == math.inf:
                # Impossible node
                dist[node] = -1
            else:
                for neighbors in graph[node]:
                    nei, wt = neighbors
                    new_dist = dist[node] + wt
                    dist[nei] = min(dist[nei], new_dist)
        
        return dist