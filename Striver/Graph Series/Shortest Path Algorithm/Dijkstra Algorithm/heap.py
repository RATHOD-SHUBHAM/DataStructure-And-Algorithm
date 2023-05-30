# Time and Sc = O(ElogV) | O(V)

import heapq
import math

class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        
        distance = [math.inf] * V
        distance[S] = 0
        
        minHeap = []
        heapq.heapify(minHeap)
        
        heapq.heappush(minHeap, (0,S)) # distance , node
        
        while minHeap:
            dist , node = heapq.heappop(minHeap)
            
            neighbor = adj[node]
            
            for nei in neighbor:
                adj_nei , weight = nei
                
                update_dist = weight + dist
                
                if update_dist < distance[adj_nei] :
                    distance[adj_nei] = update_dist
                    heapq.heappush(minHeap , (update_dist , adj_nei))
        
        
        return distance