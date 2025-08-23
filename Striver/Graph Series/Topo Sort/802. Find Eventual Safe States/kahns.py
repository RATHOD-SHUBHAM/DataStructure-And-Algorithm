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
        