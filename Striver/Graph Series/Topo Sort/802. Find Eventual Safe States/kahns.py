from collections import defaultdict
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        
        outdegree = [0] * n
        for i in range(n):
            outdegree[i] = len(graph[i])
        
        # print(outdegree)
        
        adj_nei = defaultdict(list)
        for i in range(n):
            for nei in graph[i]:
                adj_nei[nei].append(i)
        
        # print(adj_nei)
        
        # get the node with outdegree 0
        queue = []
        for i in range(n):
            if outdegree[i] == 0:
                queue.append(i)
        # print(queue)
        
        safe_node = [False] * n
        while queue:
            node = queue.pop(0)
            safe_node[node] = True
            
            for nei in adj_nei[node]:
                outdegree[nei] -= 1
                
                if outdegree[nei] == 0:
                    queue.append(nei)
        
        # print(safe_node)
        
        safeNode = []
        for i in range(n):
            if safe_node[i] == True:
                safeNode.append(i)
        
        return safeNode