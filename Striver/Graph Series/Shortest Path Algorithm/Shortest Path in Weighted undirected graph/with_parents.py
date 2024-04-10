from typing import List
import math
import heapq
import collections

class Solution:
    def shortestPath(self,n, m , edges )->List[int]:
        # code here
        graph = collections.defaultdict(list)
        weight = collections.defaultdict()
        
        for edge in edges:
            u, v, wt = edge
            
            graph[u].append(v)
            graph[v].append(u)
            
            weight[(u,v)] = wt
            weight[(v,u)] = wt
        
        
        # Dijkstra to get shortest path
        
        distance = [math.inf] * (n + 1)
        distance[1] = 0
        
        parents = [None] * (n + 1)
        parents[1] = -1
        
        minHeap = []
        heapq.heapify(minHeap)
        
        heapq.heappush(minHeap, (0,1)) # dist, src
        
        while minHeap:
            wt, node = heapq.heappop(minHeap)
            
            for nei in graph[node]:
                dist = weight[(node, nei)] # distance between node and neighbor
                
                new_wt = wt + dist
                
                if new_wt < distance[nei]:
                    distance[nei] = new_wt
                    heapq.heappush(minHeap, (new_wt, nei))
                    parents[nei] = node
            
        
        
        if distance[n] == math.inf:
            return [-1]
        
        # Grab the parents
        
        parent_ = []
        node = n
        
        while node != -1:
            parent_.append(node)
            
            node = parents[node]
        
        
        # First element is the weight and then list of nodes.
        op = [distance[-1]] + parent_[::-1]
        
        return op