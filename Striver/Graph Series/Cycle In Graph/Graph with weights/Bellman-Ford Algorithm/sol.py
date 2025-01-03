# Tc: O(V*E) | Sc: O(VE)

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        # If some node isn't possible to visit, then its distance should be 100000000(1e8). 
        dist = [10 ** 8] * V # question says 10 ^ 8 . we can habe math.inf if nothing is specified
        dist[S] = 0
        
        # Relax node for n - 1 times
        for _ in range(V-1):
            # Relax the node sequentially
            for node in edges:
                u , v , cost = node
                
                # Node relaxation
                if dist[u] != (10**8) and dist[u] + cost < dist[v]:
                    dist[v] = dist[u] + cost
                    
        # check for negative cycle
        for node in edges:
            u , v , cost = node
            
            # if the distance further reduces then there is a negative cycle
            if dist[u] != (10**8) and dist[u] + cost < dist[v]:
                return [-1] #  If the Graph contains a negative cycle then return an array consisting of only -1.
                
        return dist