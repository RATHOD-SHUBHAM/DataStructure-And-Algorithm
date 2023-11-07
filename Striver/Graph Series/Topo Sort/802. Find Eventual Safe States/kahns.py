class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        # get the neighbors
        adj_nei = collections.defaultdict(list)

        for i in range(n):
            edges = graph[i]

            for edge in edges:
                adj_nei[edge].append(i)

        # get indegree
        outdegree = [0] * n

        for i in range(n):
            edges = graph[i]

            outdegree[i] = len(edges)
        
        
        # add to queue
        queue = []
        for i in range(n):
            if outdegree[i] == 0:
                queue.append(i)   


        # topo sort
        topo_sort = []
        count = 0

        while queue:
            node = queue.pop(0)
            

            for nei in adj_nei[node]:
                outdegree[nei] -= 1

                if outdegree[nei] == 0:
                    queue.append(nei)
            
            topo_sort.append(node)
            count += 1

        
        topo_sort.sort()
        return topo_sort