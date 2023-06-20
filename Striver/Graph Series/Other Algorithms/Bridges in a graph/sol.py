# Tc: O(V + E) | Sc: O(E) # for graph creation

from collections import defaultdict
import math
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # Adj list creation ---------------------------
        graph = defaultdict(list)
        
        for edges in connections:
            ui, vi = edges
            graph[ui].append(vi)
            graph[vi].append(ui)
            
        # Tarjan Algo to find bridge ---------------------------
        step = 1
        time = [math.inf] * n
        low = [math.inf] * n
        
        visited = [False] * n
        
        bridges = [] # store the bridge
        
        # step 1:  Perform DFS
        parent = -1
        for i in range(n):
            if visited[i] == False:
                self.DFS(i, parent, time, low, step, visited, bridges, graph, n)
        
        return bridges
    
    def DFS(self, node, parent, time, low, step, visited, bridges, graph, n):
        
        # step 1: Mark the node as visited
        visited[node] = True
        
        # step 2: Update the time of insertion and lowest time of insertion
        time[node] = step
        low[node] = step
        step += 1 # increase the step count for next node
        
        # step 3: Visited neighbor
        for nei in graph[node]:
            # 3 cases
            # case 1: parent node
            if nei == parent:
                continue
            
            # case 2: visited node
            elif visited[nei] == True:
                # update low
                low[node] = min(low[node], low[nei])
            
            # case 3: not visited
            else:
                # visit the neighbor
                self.DFS(nei, node, time, low, step, visited, bridges, graph, n)
                
                # Step 4: After exploring all the neighbors
                # update low of parent
                low[node] = min(low[node], low[nei])
                
                # check for bridge
                if low[nei] <= time[node]:
                    # there is no bride
                    continue
                else:
                    # low[nei] > time[node]
                    bridges.append((node, nei))
                    
        
        return