# check cycle  - Ancestor method
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        
        ancestor = [False] * n # represents nobody is ancestor of anyone yet
        safeNode = [True] * n # initially i assume everything to be a safe node
        visited = [False] * n # leep track of visited node
        
        # Check for safe node
        for i in range(n):
            if visited[i] == False:
                checkCycle = self.dfs(i, visited, ancestor, safeNode, n, graph)
                
        
        # print(safeNode)
        
        # grab the safe state
        safe_node = []
        for i in range(n):
            if safeNode[i] == True:
                safe_node.append(i)
        
        # print(safe_node) # since i am looping in ascending order, the nodes will be sorted automatically
        
        return safe_node
    
    def dfs(self, node, visited, ancestor, safeNode, n, graph):
        
        ancestor[node] = True
        visited[node] = True
        
        # check if this has neighbors and the neighbor is a terminal node
        for nei in graph[node]:
            
            if visited[nei] == False:
                checkCycle = self.dfs(nei, visited, ancestor, safeNode, n, graph)

                if checkCycle == False:
                    safeNode[node] = False
                    break
                    
            elif visited[nei] == True:
                if ancestor[nei] == True:
                    safeNode[node] = False
                    break
                else:
                    if safeNode[nei] == False:
                        safeNode[node] = False
                        break
                    

        
        ancestor[node] = False # resetting ancestor node
        return safeNode[node]