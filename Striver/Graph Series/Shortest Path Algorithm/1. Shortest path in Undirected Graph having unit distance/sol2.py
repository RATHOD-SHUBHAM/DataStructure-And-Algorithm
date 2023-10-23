#User function Template for python3
from collections import defaultdict

class Solution:
    def shortestPath(self, edges, n, m, src):
        # dictionary to create a graph with neighbor
        graph = defaultdict(list)
        
        for edge in edges:
            node, nei = edge
            
            graph[node].append(nei)
            graph[nei].append(node)
            
        
        distance = [-1] * n
        distance[src] = 0 # distance from src to itself will be 0
        
        stack = []
        stack.append(src) # add the source node
        
        while stack:
            node = stack.pop(0)
            
            for nei in graph[node]:
                if distance[nei] == -1:
                    distance[nei] = distance[node] + 1
                    stack.append(nei)

        return distance