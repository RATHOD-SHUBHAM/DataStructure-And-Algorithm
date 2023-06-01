from typing import List
import heapq
import math
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        mod = 100000
        
        minHeap = []
        heapq.heapify(minHeap)
        heapq.heappush(minHeap, (0, start))
        
        step = [math.inf] * (10 ** 5)
        step[start] = 0
        
        
        while minHeap:
            level , node = heapq.heappop(minHeap)
            
            if node == end:
                return level
            
            for i in arr:
                cur_sum = (node * i) % mod
                if step[cur_sum] > level + 1:
                    step[cur_sum] = level + 1
                    heapq.heappush(minHeap,(level + 1, cur_sum))
        
        # print(queue)
        return -1