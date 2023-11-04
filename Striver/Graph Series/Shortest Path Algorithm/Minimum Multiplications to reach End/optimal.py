from typing import List
import heapq, math
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        mod = 100000
        
        minHeap = []
        heapq.heapify(minHeap)
        
        heapq.heappush(minHeap, (0,start))
        
        minDist = [math.inf] * (10**5)
        minDist[start] = 0

        
        while minHeap:
            level , node = heapq.heappop(minHeap)
            
            if node == end:
                return level
            
            '''
                nei node is obtained by multiplying the node with number in the array and then mod operation with 100000
            '''
            for nei in arr:
                nei_node = (node * nei) % mod
                
                nei_dist = level + 1
                
                # if new smaller dist to reach the node is obtained
                if nei_dist < minDist[nei_node]:
                    minDist[nei_node] = nei_dist
                    heapq.heappush(minHeap, (nei_dist, nei_node))
                
        return -1