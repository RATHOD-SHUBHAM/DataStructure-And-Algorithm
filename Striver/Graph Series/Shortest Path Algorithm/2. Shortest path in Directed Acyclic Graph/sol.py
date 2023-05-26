
from collections import defaultdict
import math

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        weight = defaultdict()
        
        # build graph
        for i in range(len(edges)):
            parent , child , dist = edges[i]
            
            graph[parent].append(child)
            weight[(parent,child)] = dist
        
        # print(graph)
        # print(weight)
        
        # get the shortest distance
        distance = [math.inf] * n
        distance[0] = 0
        
        queue = []
        queue.append(0)
        
        while queue:
            node = queue.pop(0)
            
            for nei in graph[node]:

                wei = weight[(node, nei)]
                parentWeight = distance[node]
                
                new_dist = wei + parentWeight
                
                update_dist = min(new_dist, distance[nei])
                
                distance[nei] = update_dist
                
                queue.append(nei)
        
        # print(distance)
                
            
        
        for i in range(n):
            if distance[i] == math.inf:
                distance[i] = -1
        
        return distance
