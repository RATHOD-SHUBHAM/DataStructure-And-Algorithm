import heapq
import math
from collections import defaultdict
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        
        
        # construct graph
        graph = defaultdict(list)
        
        for i in range(V):
            neighbor = adj[i]
            
            for nei in neighbor:
                j , wt = nei
            
                graph[i].append([wt, j])
        
        
        # Dijkstras Algorithm
        dist = [math.inf] * V
        dist[S] = 0
        
        minHeap = []
        heapq.heapify(minHeap)
        
        heapq.heappush(minHeap, (0, S)) # wt, node
        
        
        while minHeap:
            wt, node = heapq.heappop(minHeap)
            
            for nei in graph[node]:
                adj_wt, adj_node = nei
                
                new_wt = adj_wt + wt
                
                # Node Comprehension
                if new_wt < dist[adj_node]:
                    dist[adj_node] = new_wt
                    heapq.heappush(minHeap, (new_wt ,adj_node)) # wt, node
        
        return dist