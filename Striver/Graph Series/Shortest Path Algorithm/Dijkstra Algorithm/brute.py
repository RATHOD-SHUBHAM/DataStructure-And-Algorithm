import math
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        distance = [math.inf] * V # V is no of edges
        distance[S] = 0 # S is the src node
        
        queue = [(0,S)] # distance , node
        
        while queue:
            dist , node = queue.pop(0)
            
            neighbor = adj[node]
           
            for nei in neighbor:
                adj_node, weight = nei
                
                update_dist = dist + weight
                
                if update_dist < distance[adj_node]:
                    distance[adj_node] = update_dist
                    
                    queue.append((update_dist , adj_node))
                    
  
        return distance