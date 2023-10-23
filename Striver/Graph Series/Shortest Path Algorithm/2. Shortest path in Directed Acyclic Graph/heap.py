from typing import List
from collections import defaultdict
import heapq

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        # Create a graph with weights and child nodes
        for edge in edges:
            parent, child, dist = edge
            graph[parent].append([dist, child])

        
        distance = [-1] * n
    
        visited = [False] * n
        
        minHeap = []
        heapq.heapify(minHeap)
        
        # distance , src
        heapq.heappush(minHeap, (0, 0))
    
        while minHeap:
            dist, node = heapq.heappop(minHeap)
            
            # if the node is already visited - then shortest path is already explored
            if visited[node] == True:
                continue
            
            # Update the nodes distance and mark it as visited        
            distance[node] = dist
            visited[node] = True
    
            # Explore its neighbors
            for nei in graph[node]:
                wt , child = nei
    
                new_dist = dist + wt
                heapq.heappush(minHeap, (new_dist, child))
    
        return distance