# without the minSpanning tree edges

# Tc: E log E | Sc: O(E) 
import heapq
from collections import defaultdict

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):

        minHeap = []
        heapq.heapify(minHeap)
        # push any node
        heapq.heappush(minHeap , (0, 0)) #cost , node
        
        total_sum = 0
        
        visited = [False] * V
        
        while minHeap:
            cost , node = heapq.heappop(minHeap)
            
            # check if the node is not visited
            if visited[node] == False:
                
                visited[node] = True
                
                total_sum += cost
                
                for neighbor in adj[node]:
                    nei , nei_cost = neighbor
                    
                    if visited[nei] == False:
                        heapq.heappush(minHeap, (nei_cost, nei))
                        
        # print(total_sum)
        return total_sum