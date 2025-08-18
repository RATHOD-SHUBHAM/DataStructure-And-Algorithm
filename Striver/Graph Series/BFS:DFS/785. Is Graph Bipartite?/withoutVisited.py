class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        # Color the nodes on the go
        color = [None] * n

        queue = collections.deque()

        # Traverse across all the node
        for i in range(n):
            if color[i] != None:
                # If the node has already been colored and explored
                continue
            
            queue.append(i)
            color[i] = True

            
            # Explore all its neighbors level by level
            while queue:
                node = queue.popleft()

                for nei in graph[node]:
                    # If the nei is not visited, color the nei with a different color
                    if color[nei] == None:
                        color[nei] = not color[node] # Using a opposite color
                        queue.append(nei)
                    
                    else:
                        # If the nei was already visited, it cannot have same color
                        if color[node] == color[nei]:
                            return False
            
        return True
    
