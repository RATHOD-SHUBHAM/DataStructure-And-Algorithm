# Tc and Sc: O(V + E)

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        
        visited = [False] * n
        safeNode = [False] * n
        
        # *-----------Helper Code--------------------
        def dfs(i):
            # mark this node as visited
            visited[i] = True
            
            
            flag = True # keep track if any cycle is present in that path
            for nei in graph[i]:
                if visited[nei] == False:
                    cyclePresent = dfs(nei)
                    
                    # if at any path there is a cycle. then we cant proceed
                    if cyclePresent == False:
                        flag = False
                        break
                else:
                    if visited[nei] == True and safeNode[nei] == False:
                        safeNode[i] = False
                        return False
                    # elif visited[nei] == True and safeNode[nei] == True:
                    #     safeNode[i] = True
                    #     return True # this will be anyways take care by flag # redundant code
                              
            # if this is a terminal node
            if graph[i] == []:
                safeNode[i] = True
                return True
            else:
                if flag == True:
                    safeNode[i] = True
                    return True
                else:
                    safeNode[i] = False
                    return False
        
        # *-----------Main Code----------------------
        for i in range(n):
            if not visited[i]:
                cyclePresent = dfs(i)
                
                if cyclePresent == True:
                    safeNode[i] = True
        
        all_safe_nodes = []
        for i in range(n):
            if safeNode[i] == True:
                all_safe_nodes.append(i)
        
        return all_safe_nodes