
from typing import List
import collections
import math

class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        # Build Graph
        graph = collections.defaultdict(list)
        for edge in edges:
            node, nei, wt = edge
            graph[node].append((nei, wt))
        
        dist = [math.inf] * V
        dist[0] = 0 # Start node
        
        queue = collections.deque()
        queue.append(0)
        
        # BFS
        while queue:
            node = queue.popleft()
            
            for neighbors in graph[node]:
                nei, wt = neighbors
                
                nei_dst = dist[node] + wt
                
                # IF nei can be reached at much shorter dist, update the nei distance
                if nei_dst < dist[nei]:
                    queue.append(nei)
                    dist[nei] = nei_dst
        
        for i in range(V):
            if dist[i] == math.inf:
                dist[i] = -1
        
        return dist
