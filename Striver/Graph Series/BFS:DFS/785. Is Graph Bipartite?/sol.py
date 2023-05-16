class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        
        color = [None] * n
        queue = []
        
        for node in range(n):
            # BFS
            if color[node] is None:
                color[node] = True
                queue.append(node)
                
            while queue:
                cur_node = queue.pop(0)

                for nei in graph[cur_node]:

                    if color[nei] is None:
                        queue.append(nei)
                        color[nei] = not color[cur_node]

                    elif color[nei] == color[cur_node]:
                        return False

                    else:
                        continue
                            
        return True