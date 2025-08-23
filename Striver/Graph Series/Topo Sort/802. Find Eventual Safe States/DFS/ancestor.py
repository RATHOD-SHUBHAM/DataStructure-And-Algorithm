class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        ancestor = [False] * n # Helps keep track of cycle
        visited = [False] * n

        # Initally we assume everything to be safe node
        safeNode = [True] * n

        # Start Exploration
        for i in range(n):
            if visited[i] == True:
                continue
            
            isSafe = self.dfs(i, ancestor, visited, safeNode, graph)

            if isSafe == False:
                safeNode[i] = False

        safe_states = []
        for i in range(n):
            if safeNode[i] == True:
                safe_states.append(i)
        
        return safe_states
    
    
    def dfs(self, node, ancestor, visited, safeNode, graph):
        # Mark the node as visited
        visited[node] = True

        # Make it as a ancestor for its neighbors
        ancestor[node] = True

        # Explore its neighbors
        for nei in graph[node]:
            if visited[nei] == False:
                # If nei is not visited , then explore
                isSafe = self.dfs(nei, ancestor, visited, safeNode, graph)

                if isSafe == False:
                    safeNode[node] = False
                    break # we dont have to explore further
            
            else:
                # If the nei was visited before and is an ancestor of current, then there is a cycle
                if ancestor[nei] == True:
                    # Since there is a cycle, current node cannont be safe node
                    safeNode[node] = False
                    break # we dont have to explore further
                else:
                    if safeNode[nei] == False:
                        # If the nei is not a safe node, then current node cannot be a safe node
                        safeNode[node] = False
                        break # we dont have to explore further
        

        # Unmark the node as ancestor, since it has finished exploring all its neighbor
        ancestor[node] = False

        return safeNode[node]


