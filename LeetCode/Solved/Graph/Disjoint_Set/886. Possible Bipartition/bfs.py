# BFS
from collections import defaultdict
class Solution:
    def buildGraph(self, dislikes):
        graph = defaultdict(list)

        for i in dislikes:
            u ,  v = i
            graph[u].append(v)
            graph[v].append(u)

        return graph

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = self.buildGraph(dislikes)
        # print(graph)

        # BFS
        queue = []
        color = [None] * (n + 1)

        for i in range(1, n + 1):
            
            if color[i] != None:
                continue
            
            color[i] = True #red
            queue.append(i)

            while queue:
                node = queue.pop(0)

                for nei in graph[node]:
                    if color[nei] == None:
                        color[nei] = not color[node]
                        queue.append(nei)
                    else:
                        if color[nei] == color[node]:
                            return False
        return True     