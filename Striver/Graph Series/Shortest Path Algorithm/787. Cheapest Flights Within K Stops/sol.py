class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for flight in flights:
            u, v, dt = flight
            graph[u].append((v,dt))

        
        minHeap = []
        heapq.heapify(minHeap)

        dist = [math.inf] * n
        dist[src] = 0

        heapq.heappush(minHeap, (0,0,src)) # stop, distance, src

        while minHeap:
            stop, dt, node = heapq.heappop(minHeap)

            if stop > k and node != dst:
                continue

            for neighbor in graph[node]:
                nei, nei_dt = neighbor

                new_dt = nei_dt + dt

                if new_dt < dist[nei]:
                    dist[nei] = new_dt
                    heapq.heappush(minHeap, (stop+1, new_dt, nei))
            
        return -1 if dist[dst] == math.inf else dist[dst]