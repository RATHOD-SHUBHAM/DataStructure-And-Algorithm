from collections import defaultdict
import math
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        src = 0
        dst = n - 1
        
        mod = (10**9 + 7)
        
        # build graph
        graph = defaultdict(list)
        time = defaultdict()
        for i in roads:
            src, dst , cost = i
            graph[src].append(dst)
            graph[dst].append(src)
            time[(src, dst)] = cost
            time[(dst, src)] = cost
        
        # print(graph)
        # print(time)
        
        # Dijstras
        distance = [math.inf] * n
        distance[0] = 0
        
        minHeap = []
        heapq.heapify(minHeap)
        heapq.heappush(minHeap, (0,0))
        
        node_count = [0] * n
        node_count[0] = 1
        
        while minHeap:
            dist , node = heapq.heappop(minHeap)
            
            for nei in graph[node]:
                cost = time[(node, nei)]
                
                updated_dist = cost + dist
                
                if updated_dist < distance[nei]:
                    distance[nei] = updated_dist
                    heapq.heappush(minHeap, (updated_dist , nei))
                    node_count[nei] = node_count[node]
                
                elif updated_dist == distance[nei]:
                    node_count[nei] = (node_count[nei] + node_count[node])
                    
        # print(node_count)
        
        return 1 if node_count[-1] == 0 else node_count[-1] % mod