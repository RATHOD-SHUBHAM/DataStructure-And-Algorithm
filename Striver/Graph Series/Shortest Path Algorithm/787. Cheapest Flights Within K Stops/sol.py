class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build Graph
        graph = collections.defaultdict(list)
        for flight in flights:
            u, v, dist = flight
            graph[u].append((v, dist))
        
        minHeap = []
        heapq.heapify(minHeap)

        heapq.heappush(minHeap, (0,0,src)) # stop, dist, src

        dist = [math.inf] * n
        dist[src] = 0

        while minHeap:
            stop, dt, node = heapq.heappop(minHeap)

            # Check if we have exceded K hops
            if stop > k and node != dst:
                continue
            
            # Explore the neighbors
            for neighbor in graph[node]:
                nei, nei_dt = neighbor
            
                new_dt = dt + nei_dt

                if new_dt < dist[nei]:
                    dist[nei] = new_dt
                    heapq.heappush(minHeap, (stop + 1, new_dt, nei))
        
        return -1 if dist[dst] == math.inf else dist[dst]