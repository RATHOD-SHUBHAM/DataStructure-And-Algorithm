class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        
        color = [None] * n
        visited = set()
        
        queue = []
        
        for i in range(n):
            
            if i not in visited:
                queue.append(i)
                visited.add(i)
                color[i] = True

                while queue:
                    node = queue.pop(0)

                    for nei in graph[node]:
                        if nei not in visited:
                            color[nei] = not color[node]
                            queue.append(nei)
                            visited.add(nei)
                        else:
                            if color[nei] == color[node]:
                                return False

        return True