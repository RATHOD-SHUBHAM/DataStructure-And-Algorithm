# DFS
class Solution:
    def buildGraph(self, dislikes):
        graph = defaultdict(list)

        for i in dislikes:
            u , v = i

            graph[u].append(v)
            graph[v].append(u)
        
        return graph

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = self.buildGraph(dislikes)
        print(graph)

        color = [None] * (n + 1)

        for i in range(1, n + 1):
            isValid = self.dfs(i, graph, color, n)
            
            if isValid == False:
                    return False

        return True
    
    def dfs(self, cur_idx, graph, color, n):
        if cur_idx == n + 1:
            return True
        
        if color[cur_idx] == None:
            color[cur_idx] = True

        for nei in graph[cur_idx]:
            if color[nei] == None:
                color[nei] = not color[cur_idx]

                isValid = self.dfs(nei, graph, color, n)

                if isValid == False:
                    return False
            else:
                if color[nei] == color[cur_idx]:
                    return False
        
        return True