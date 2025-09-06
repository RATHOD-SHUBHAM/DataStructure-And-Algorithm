class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build Graph
        graph = collections.defaultdict(list)
        for tme in times:
            u, v, wt = tme
            graph[u].append((v, wt))
        
        minHeap = []
        heapq.heapify(minHeap)

        heapq.heappush(minHeap, (0, k)) # time, src

        dist = [math.inf] * (n+1) # 1 based index
        dist[k] = 0

        while minHeap:
            wt, node = heapq.heappop(minHeap)

            for neighbor in graph[node]:
                nei, nei_wt = neighbor

                new_wt = wt + nei_wt

                if new_wt < dist[nei]:
                    dist[nei] = new_wt
                    heapq.heappush(minHeap, (new_wt, nei)) # time, src
        

        dist = dist[1: ] # 1 based index
        if math.inf in dist:
            return -1
        else:
            return max(dist)