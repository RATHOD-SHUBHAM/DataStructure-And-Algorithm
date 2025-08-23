class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        
        visited = [False] * n
        safeNode = [False] * n

        for i in range(n):
            if visited[i] == True:
                continue
            
            isSafe = self.dfs(i, visited, safeNode, graph)

            if isSafe == False:
                safeNode[i] = False
        
        safe_states = []
        for i in range(n):
            if safeNode[i] == True:
                safe_states.append(i)
        
        return safe_states
    
    def dfs(self, node, visited, safeNode, graph):
        # Mark the node as visited
        visited[node] = True

        # Explore its neighbors
        for nei in graph[node]:
            if visited[nei] == False:
                # If nei is not visited , then explore
                isSafe = self.dfs(nei, visited, safeNode, graph)

                if isSafe == False:
                    safeNode[node] = False
                    return False # we dont have to explore further
            
            else:
                # if neighbor was previously visited and is not a safe node
                if safeNode[nei] == False:
                    safeNode[node] = False
                    return False # we dont have to explore further
        
        # If we reach here, all neighbors are safe or no neighbors exist
        safeNode[node] = True
        return True
        