from typing import List
from collections import defaultdict
import heapq

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        weights = defaultdict()
        
        for edge in edges:
            u, v, wt = edge
            graph[u].append(v)
            weights[(u,v)] = wt
        
        distance = [-1] * n
        distance[0] = 0 # src
        
        # Dijkstras algorithm
        minHeap = []
        heapq.heapify(minHeap)
        
        heapq.heappush(minHeap, (0, 0)) # dist, src
        
        while minHeap:
            wt, node = heapq.heappop(minHeap)
            
            for nei in graph[node]:
                nei_wt = weights[(node, nei)]
                
                new_wt = wt + nei_wt
                
                if distance[nei] == -1:
                    distance[nei] = new_wt
                    heapq.heappush(minHeap, (new_wt, nei))
                else:
                    if new_wt < distance[nei]:
                        distance[nei] = new_wt
                        heapq.heappush(minHeap, (new_wt, nei))
        
        return distance