# Tc: O(N + ElogV) | Sc: O(V + E)

from collections import defaultdict
import heapq
import math

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # network of n nodes, labeled from 1 to n and not 0 - n -1
        graph = defaultdict(list)
        time = defaultdict()
        for i in times:
            src , dst , cost = i
            graph[src - 1].append(dst - 1)
            time[(src - 1,dst - 1)] = cost
        
        # print(graph)
        # print(time)
        
        # if the src has no other nodes then it cannot traverse the entire graph
        if k - 1 not in graph:
            return -1
        
        
        distance = [math.inf] * n
        distance[k - 1] = 0
        
        minHeap = []
        heapq.heapify(minHeap)
        
        heapq.heappush(minHeap, (0 , k - 1)) 
        
        while minHeap:
            dist , node = heapq.heappop(minHeap)
            
            for nei in graph[node]:
                child_cost = time[(node, nei)] # cost
                
                updated_cost = child_cost + dist
                
                if updated_cost < distance[nei]:
                    distance[nei] = updated_cost
                    heapq.heappush(minHeap, (updated_cost , nei))
                    
        # print(distance)
        if math.inf in distance:
            return -1
        else:
            return max(distance)
        
        