from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        #Code here

        visited = [False] * V

        parent = -1

        for i in range(V):
            if visited[i] == False:
                cyclePresent = self.checkForCycle(i, parent, visited, V, adj)
                
                if cyclePresent:
                    return 1

        return 0

    def checkForCycle(self, i, parent, visited, V, adj):

        queue = [[i, parent]]


        while queue:
            
            node, parent_node = queue.pop(0)
            
            visited[node] = True
            
            for child in adj[node]:
                if child == parent_node:
                    continue
                
                if visited[child] == True:
                    return True
                
                queue.append((child, node))
                        
        return False