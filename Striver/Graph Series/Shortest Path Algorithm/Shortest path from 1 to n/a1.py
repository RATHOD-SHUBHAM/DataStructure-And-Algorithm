import math
import heapq
import collections

class Solution:
    def minimumStep (self, n):
        # build graph
        graph = collections.defaultdict(list)
        
        for i in range(1, n + 1):
            if 3*i < n + 1:
                graph[i].append(3*i)
            if i + 1 < n+1:
                graph[i].append(i+1)
        
        print(graph)
        
        
        # Dijkstras algorith
        distance = [math.inf] * (n+1)
        distance[1] = 0
        
        minHeap = []
        heapq.heapify(minHeap)
        
        heapq.heappush(minHeap, (0, 1)) # dist, src
        
        while minHeap:
            wt, node = heapq.heappop(minHeap)
            
            for nei in graph[node]:
                new_wt = wt + 1
                
                if new_wt < distance[nei]:
                    distance[nei] = new_wt
                    heapq.heappush(minHeap, (new_wt, nei))
        
        return distance[-1]



# -------------  Optimal Solution ----------


# Reverse engineering
class Solution:
    def minimumStep (self, n):
        steps = 0
        
        while n > 1:
            # check if this is divisible by 3
            if n % 3 == 0:
                n = n // 3
            else:
                # else subtract 1
                n -= 1
            
            steps += 1
        
        return steps