# No of shortest path to the destination

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        # Graph Creation ------------------------------------------------
        graph = collections.defaultdict(list)
        distance = collections.defaultdict()

        for road in roads:
            u , v , t = road

            # Graph is bidirectional
            graph[u].append(v)
            graph[v].append(u)

            distance[(u,v)] = t
            distance[(v,u)] = t
        
        
        # Shortest Path ------------------------------------------------
        minHeap = []
        heapq.heapify(minHeap)

        heapq.heappush(minHeap, (0,0)) # dist , node

        minDist = [math.inf] * n
        minDist[0] = 0
        
        # Keep track of no of ways we can reach at a node
        no_of_ways = [0] * n
        no_of_ways[0] = 1 # there is only one way to reach start node

        while minHeap:
            dist, node = heapq.heappop(minHeap)

            for nei in graph[node]:
                nei_dist = distance[(node, nei)]

                new_dist = dist + nei_dist


                # a node can be reached at a smaller distance than the previous one
                if new_dist < minDist[nei]:
                    heapq.heappush(minHeap, (new_dist , nei))
                    minDist[nei] = new_dist

                    # no of ways to reach a neighbor depends on no of ways to reach a node
                    no_of_ways[nei] = no_of_ways[node]
                
                elif new_dist == minDist[nei]:
                    # new path is getting added to reach a node
                    no_of_ways[nei] += no_of_ways[node]

        
        mod = (10 ** 9) + 7

        return (no_of_ways[n-1] % mod)