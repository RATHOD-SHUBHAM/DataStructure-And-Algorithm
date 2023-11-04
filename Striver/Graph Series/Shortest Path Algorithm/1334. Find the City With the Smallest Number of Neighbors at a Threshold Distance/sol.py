from collections import defaultdict
import math

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # build graph ----------
        graph = [[math.inf for _ in range(n)] for _ in range(n)]
        for i in range(n):
            graph[i][i] = 0
            
        for edge in edges:
            i , j , cost = edge
            
            graph[i][j] = cost
            graph[j][i] = cost
        
        # print(graph)
        
        # FLOYD WARSHAL: multi source shortest path ----------------
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    cur_cost = graph[i][k] + graph[k][j]
                    graph[i][j] = min(graph[i][j] , cur_cost)
        
        # print(graph)
        
        # # Get the number of cities that are reachable whose distance is at most distanceThreshold --------------------
        distance = [0] * n

        for i in range(n):
            count = 0
            for j in range(n):
                if i == j:
                    continue
                
                if graph[i][j] <= distanceThreshold:
                    count += 1 
            
            distance[i] = count
        
        # print(distance)
        
        # Return the city with the smallest number of cities that are reachable --------------------
        minVal = min(distance)
        minIdx = distance.index(minVal)
        
        for i in range(n):
            if distance[i] <= minVal:
                minIdx = i
                minVal = distance[i]
        
        return minIdx
        