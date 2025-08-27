# Tc and Sc: O(V + E)

import collections
import math

class Solution:
    def shortestPath(self, adj, src):
        n = len(adj)
        
        # BFS
        queue = collections.deque()
        queue.append((src, 0)) # Node, dist
        
        dist = [-1] * n 
        dist[src] = 0
        
        while queue:
            node, dst = queue.popleft()
            
            for nei in adj[node]:
                # If the nei is not explored
                if dist[nei] == -1:
                    new_dst = dst + 1
                    dist[nei] = new_dst
                    queue.append((nei, new_dst))
        
        return dist