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
    

# ---------------------------------------- DFS ----------------------------------------

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
        


# ---------------------------------------- BFS (Kahn's Algo) ----------------------------------------
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        # Build adjlist for outdegree neighbor nodes
        adj_list = collections.defaultdict(list)
        for i in range(n):
            for j in graph[i]:
                adj_list[j].append(i)
        # print(adj_list)

        # Step 1: Get the outdegree of the nodes
        outdegree = [0] * n
        for i in range(n):
            outdegree[i] = len(graph[i])
        # print(outdegree)
        

        # Step 2: Get all the nodes with no preq
        queue = collections.deque()
        for i in range(n):
            if outdegree[i] == 0:
                queue.append(i)
        
        # Iterate over the neighbors and unlock them
        count = 0
        topo_sort = []
        while queue:
            node = queue.popleft()

            for nei in adj_list[node]:
                outdegree[nei] -= 1

                if outdegree[nei] == 0:
                    queue.append(nei)
            
            count += 1
            topo_sort.append(node)
        
        # print(topo_sort)
        
        topo_sort.sort()
        return topo_sort
        