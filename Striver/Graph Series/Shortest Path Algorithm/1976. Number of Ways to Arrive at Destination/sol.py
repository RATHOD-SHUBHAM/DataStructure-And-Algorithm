"""
In many graphs there are multiple shortest ways to reach intermediate nodes, 
and those should propagate forward. In other words, you need to know, for every node, 
how many shortest paths reach it, not just for dst

"""

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # build Graph
        graph = collections.defaultdict(list)
        # bi-directional roads -> bi-directional edges
        for road in roads:
            u, v, tme = road
            graph[u].append((v, tme))
            graph[v].append((u, tme))

        
        MOD = (10 ** 9) + 7
        src = 0
        dst = n-1

        minHeap = []
        heapq.heapify(minHeap)

        heapq.heappush(minHeap, (0, src)) # Time , src

        dist = [math.inf] * n
        dist[src] = 0

        #  When you find a shorter path to an intermediate node, you need to update how many ways there are to reach that node.
        ways = [0] * n
        ways[src] = 1 # no of ways to reach destination

        while minHeap:
            t, node = heapq.heappop(minHeap)

            for neighbor in graph[node]:
                nei, nei_t = neighbor

                new_t = nei_t + t

                # If new shortest path was found
                if new_t < dist[nei]:
                    dist[nei] = new_t
                    ways[nei] = ways[node] # no of ways to reach this node is same as no of nodes to reach previous node
                    heapq.heappush(minHeap, (new_t, nei))
                
                elif new_t == dist[nei]:
                    # add this path to the current node path
                    ways[nei] = ways[node] + ways[nei]
            
        return ways[dst] % MOD

            