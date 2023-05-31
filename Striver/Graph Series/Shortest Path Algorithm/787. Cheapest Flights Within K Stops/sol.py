from collections import defaultdict
import math

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        prices = defaultdict()
        for i in flights:
            sc , dest , price = i
            
            # build graph
            graph[sc].append(dest)
            
            # map prices
            prices[(sc, dest)] = price
            
        # print(graph)
        # print(prices)
        
        distance = [math.inf] * n
        distance[src] = 0
        
        queue = [(0 , src , 0)] # layover, node, distance
        
        while queue:
            layover , node , dist = queue.pop(0)
            
            if layover > k and node != dst:
                continue
            
            for neighbor in graph[node]:
                cost = prices[(node , neighbor)]
                
                total_cost = cost + dist
                
                if total_cost < distance[neighbor]:
                    distance[neighbor] = total_cost
                    queue.append((layover + 1, neighbor, total_cost))
        
        # print(distance)
        return distance[dst] if distance[dst] != math.inf else -1