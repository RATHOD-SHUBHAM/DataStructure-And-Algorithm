from typing import List
import collections
import math
import heapq

class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        # Build Graph
        graph = collections.defaultdict(list)
        for edge in edges:
            node, nei, wt = edge
            graph[node].append((nei, wt))
        
        
        minHeap = []
        heapq.heapify(minHeap)
        
        heapq.heappush(minHeap, (0,0)) # dist, node
        
        dist = [math.inf] * V
        visited = [False] * V
        
        while minHeap:
            dst, node = heapq.heappop(minHeap)
            
            if visited[node] == True:
                continue
        
            # Mark the node as visited
            visited[node] = True
            dist[node] = dst
            
            # Explore its neighbors
            for neighbors in graph[node]:
                nei, wt = neighbors
                
                nei_dst = dist[node] + wt
                
                heapq.heappush(minHeap, (nei_dst, nei)) # dist, node
                
        
        for i in range(V):
            if dist[i] == math.inf:
                dist[i] = -1
        
        return dist