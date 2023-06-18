import math
import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        time = defaultdict()
        
        for i in times:
            
            ui, vi, wi = i
            
            graph[ui].append(vi)
            time[(ui, vi)] = wi

        
        minHeap = []
        heapq.heapify(minHeap)
        heapq.heappush(minHeap, (0, k))
        
        distance = [math.inf] * (n+1)
        distance[k] = 0
        
        while minHeap:
            t , node = heapq.heappop(minHeap)
            
            
            for nei in graph[node]:
                nei_time = time[(node, nei)]
                
                updated_time = nei_time + t
                
                if updated_time < distance[nei]:
                    distance[nei] = updated_time
                    heapq.heappush(minHeap, (updated_time, nei))
        
        
        if math.inf in distance[1 :]:
            return -1
        else:
            return max(distance[1:])