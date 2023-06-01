import heapq
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        mod = 100000
        
        minHeap = []
        heapq.heapify(minHeap)
        heapq.heappush(minHeap, (0, start))
        
        visited = set()
        
        while minHeap:
            level , node = heapq.heappop(minHeap)
            
            if node == end:
                return level
                
            if node in visited:
                continue
            
            visited.add(node)
            
            for i in arr:
                cur_sum = (node * i) % mod
                heapq.heappush(minHeap,(level + 1, cur_sum))
        
        # print(queue)
        return -1