# with the minSpanning tree edges

import heapq
from collections import defaultdict

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):

        minHeap = []
        heapq.heapify(minHeap)
        # push any node
        heapq.heappush(minHeap , (0, 0, -1)) #cost , node , parent
        
        total_sum = 0
        
        visited = [False] * V
        
        # store the edges of spanning tree
        minSpan = []
        
        while minHeap:
            cost , node, parent = heapq.heappop(minHeap)
            
            # check if the node is not visited
            if visited[node] == False:
                
                visited[node] = True
                
                total_sum += cost
                
                for neighbor in adj[node]:
                    nei , nei_cost = neighbor
                    
                    if visited[nei] == False:
                        heapq.heappush(minHeap, (nei_cost, nei, node))
                        
                if parent != -1:
                    minSpan.append((node, parent))
                    
                        
        # print(total_sum)
        # print(minSpan)
        return total_sum