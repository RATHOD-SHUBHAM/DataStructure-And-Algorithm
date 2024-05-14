'''
- We have to reach a node before a particular node - not at the same time or after the node. Because, we might remove the current node then remaining node becomes stranded.

- We will not consider starting node to be articulation point, becasue even if we remove the starting node, the other component will be like a single unit or province.
    If the starting node has one child, then it doesnt make sense to remove the parent - the remaining node will still be one component.
    If the starting node has more than one child then, we will consider it to be a articulation point.

- If neighbor is visited - we dont look at the lowest time, insted we look at the time of creation.
because we assume the node might be removed, and if the node is removed then we cannot reach the other node that we could via the current node.
Hence we dont look at the lowest time, we consider the node time.
'''
import math
class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def articulationPoints(self, V, adj):
        # Tarjans algorithm for articulation point
        visited = [False] * V
        
        time = [math.inf] * V
        low = [math.inf] * V
        step = 1
        
        articulation_point = [0] * V
        
        parent = -1
        
        for i in range(V):
            if visited[i] == False:
                self.dfs(i, parent, time, low, step, visited, articulation_point, adj)
                
        
        # Get the points ----------------------------
        points = []
        for i in range(V):
            if articulation_point[i] == 1:
                points.append(i)
        
        
        if len(points) == 0:
            return [-1]
        else:
            return points
        

            
    def dfs(self, node, parent, time, low, step, visited, articulation_point, adj):
        child = 0 # Parent articulation check
        
        # step 1: mark the node as visited
        visited[node] = True
        
        # step 2: update the time and low
        time[node] = step
        low[node] = step
        step += 1
        
        # step 3: perform dfs on nei
        for nei in adj[node]:
            # 3 cases
            # case 1: when nei is parent
            if nei == parent:
                continue
            elif visited[nei] == True:
                # case 2: when nei is visited
                low[node] = min(low[node] , time[nei])
            else:
                # when node is not visited
                self.dfs(nei, node, time, low, step, visited, articulation_point, adj)
                
                # step 4: Return to parent
                # update low
                low[node] = min(low[node], low[nei])
                
                # check for articulation point
                if parent != -1 and low[nei] >= time[node]:
                    articulation_point[node] = 1

                # increase the child count
                child += 1

        # Parent articulation check -------------------
        if parent == -1 and child > 1:
            articulation_point[node] = 1
                
        return