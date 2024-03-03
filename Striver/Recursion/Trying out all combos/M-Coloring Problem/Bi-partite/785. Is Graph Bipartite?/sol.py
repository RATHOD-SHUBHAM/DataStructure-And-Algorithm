class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        color = [None] * n

        queue = []

        for node in range(n):
            if color[node] == None:
                color[node] = True
                queue.append(node)
            

            while queue:
                node = queue.pop(0)

                for nei in graph[node]:

                    if color[nei] == None:
                        color[nei] = not color[node]
                        queue.append(nei)
                    
                    elif color[nei] == color[node]:
                        return False
            
        return True

