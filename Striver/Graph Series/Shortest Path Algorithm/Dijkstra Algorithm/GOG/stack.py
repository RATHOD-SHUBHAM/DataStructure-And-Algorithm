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
        
        
        # Dijstras Algorithm
        dist = [math.inf] * V
        dist[S] = 0
        
        stack = [[0, S]] # wt, src node
        
        while stack:
            wt, node = stack.pop(0)
            
            for nei in graph[node]:
                adj_wt, adj_node = nei
                
                new_wt = adj_wt + wt
                
                # Node Comprehension
                if new_wt < dist[adj_node]:
                    dist[adj_node] = new_wt
                    stack.append([new_wt ,adj_node])
        
        return dist