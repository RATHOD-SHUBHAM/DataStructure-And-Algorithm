def bellman_ford(self, V, edges, S):
        #code here
        # If some node isn't possible to visit, then its distance should be 100000000(1e8). 
        dist = [10 ** 8] * V
        dist[S] = 0
        
        for _ in range(V-1):
            for node in edges:
                u , v , cost = node
                
                if dist[u] + cost < dist[v]:
                    dist[v] = dist[u] + cost
                    
        # check for negative cycle
        for node in edges:
            u , v , cost = node
            
            # if the distance further reduces then there is a negative cycle
            if dist[u] + cost < dist[v]:
                return [-1] #  If the Graph contains a negative cycle then return an array consisting of only -1.
                
        return dist