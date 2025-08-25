class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        # Build the graph
        graph = collections.defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        shortest_cycle = math.inf
        
        for i in range(n):
            
            cycle_len = self.bfs(i, graph, n)

            shortest_cycle = min(shortest_cycle, cycle_len)

        return shortest_cycle if shortest_cycle != math.inf else -1

    def bfs(self, node, graph, n):
        queue = collections.deque()
        queue.append((node, -1))

        dist = [math.inf] * n
        dist[node] = 0

        shortest_cycle = math.inf

        while queue:
            node, par = queue.popleft()

            for nei in graph[node]:
                # Not visited before
                if dist[nei] == math.inf:
                    dist[nei] = dist[node] + 1
                    queue.append((nei, node))
                # Node visited before and is not parent
                elif nei != par:
                    cycle_len = dist[node] + dist[nei] + 1
                    shortest_cycle = min(shortest_cycle, cycle_len)
        
        return shortest_cycle



