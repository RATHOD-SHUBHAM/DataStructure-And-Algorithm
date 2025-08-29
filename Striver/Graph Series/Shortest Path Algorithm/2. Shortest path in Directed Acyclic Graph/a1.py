# ------------------------------ Kahn's Algorithm + Relaxation ------------------------------
"""
In Topological sorting, we are guranteed that before reaching a child node 
all of its parent nodes are explored.
Thereby we would have explored all possibility of reaching the child node, as no later nodes can go back to child node
"""

from typing import List
import collections
import math

class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        # Build Graph
        graph = collections.defaultdict(list)
        indegree = [0] * V
        for edge in edges:
            node, nei, wt = edge
            graph[node].append((nei, wt))
            indegree[nei] += 1
        
        queue = collections.deque()
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
        
        topo_sort = []
        while queue:
            node = queue.popleft()
            
            for neighbors in graph[node]:
                nei, wt = neighbors
                
                indegree[nei] -= 1
                
                if indegree[nei] == 0:
                    queue.append(nei)
            
            topo_sort.append(node)
        
        # Get distance
        dist = [math.inf] * V
        dist[0] = 0
        
        for node in topo_sort:
            if dist[node] == math.inf:
                # Impossible node
                dist[node] = -1
            else:
                for neighbors in graph[node]:
                    nei, wt = neighbors
                    new_dist = dist[node] + wt
                    dist[nei] = min(dist[nei], new_dist)
        
        return dist
    
# ------------------------------ BFS (Not Optimal) ------------------------------
"""
We explore nodes level by level, and if we reach a node at a shorter distance we update its distance and add it to the queue
"""

from typing import List
import collections
import math

class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        # Build Graph
        graph = collections.defaultdict(list)
        for edge in edges:
            node, nei, wt = edge
            graph[node].append((nei, wt))
        
        dist = [math.inf] * V
        dist[0] = 0 # Start node
        
        queue = collections.deque()
        queue.append(0)
        
        # BFS
        while queue:
            node = queue.popleft()
            
            for neighbors in graph[node]:
                nei, wt = neighbors
                
                nei_dst = dist[node] + wt
                
                # IF nei can be reached at much shorter dist, update the nei distance
                if nei_dst < dist[nei]:
                    queue.append(nei)
                    dist[nei] = nei_dst
        
        for i in range(V):
            if dist[i] == math.inf:
                dist[i] = -1
        
        return dist
    
    
# ------------------------------ Heap (Not Optimal) ------------------------------

'''
In BFS we can have multiple entries of same node in queue, thereby increasing the time complexity
To avoid that we can use MinHeap and a visited array to keep track of visited nodes
'''

from typing import List
import collections
import math
import heapq

class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        # Build Graph
        graph = collections.defaultdict(list)
        for edge in edges:
            node, nei, wt = edge
            graph[node].append((nei, wt))
        
        
        minHeap = []
        heapq.heapify(minHeap)
        
        heapq.heappush(minHeap, (0,0)) # dist, node
        
        dist = [math.inf] * V
        visited = [False] * V
        
        while minHeap:
            dst, node = heapq.heappop(minHeap)
            
            if visited[node] == True:
                continue
        
            # Mark the node as visited
            visited[node] = True
            dist[node] = dst
            
            # Explore its neighbors
            for neighbors in graph[node]:
                nei, wt = neighbors
                
                nei_dst = dist[node] + wt
                
                heapq.heappush(minHeap, (nei_dst, nei)) # dist, node
                
        
        for i in range(V):
            if dist[i] == math.inf:
                dist[i] = -1
        
        return dist
    
# ------------------------------ Dijkstra's algorithm ------------------------------
"""
Instead of visited array we can use the distance array to check if we have already found a shorter path to the node
"""

from typing import List
import collections
import math
import heapq

class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        # Build Graph
        graph = collections.defaultdict(list)
        for edge in edges:
            node, nei, wt = edge
            graph[node].append((nei, wt))
        
        
        minHeap = []
        heapq.heapify(minHeap)
        
        heapq.heappush(minHeap, (0,0)) # dist, node
        
        dist = [math.inf] * V
        dist[0] = 0
        
        while minHeap:
            dst, node = heapq.heappop(minHeap)
            
            # Explore its neighbors
            for neighbors in graph[node]:
                nei, wt = neighbors
                
                nei_dst = dist[node] + wt
                
                if nei_dst < dist[nei]:
                
                    dist[nei] = nei_dst
                        
                    heapq.heappush(minHeap, (nei_dst, nei)) # dist, node
                
        
        for i in range(V):
            if dist[i] == math.inf:
                dist[i] = -1
        
        return dist