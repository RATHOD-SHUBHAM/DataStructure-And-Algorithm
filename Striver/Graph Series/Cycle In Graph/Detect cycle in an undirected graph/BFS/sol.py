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
                if visited[child] == False:
                    queue.append([child, node])
                else:
                    # a node can only be visited before if they have a common parent
                    if child != parent_node:
                        return True
                        
        return False