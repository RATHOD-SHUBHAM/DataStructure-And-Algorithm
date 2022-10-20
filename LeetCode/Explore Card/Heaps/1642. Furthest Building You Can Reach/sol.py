# https://www.youtube.com/watch?v=nztc9MKaask&ab_channel=CodewithAlisha
# logic: use ladder for the longerst jump

# Tc: O(NlogN)
# Sc: O(N)

import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minHeap = []
        heapq.heapify(minHeap) #O(log n)
        n = len(heights)
        
        # O(n)
        for i in range(n-1):
            jump = heights[i+1] - heights[i]
            
            # there is no need of a brick or a ladder
            if jump <= 0:
                continue
            
            # add jump to heap
            heapq.heappush(minHeap , -jump)
            
            # the number of brick used
            bricks = bricks - jump
            
            # check if i can move further
            if bricks < 0 and ladders <= 0:
                return i
            
            
            if bricks < 0:
                bricks = bricks + heapq.heappop(minHeap) * -1
                ladders -= 1
                
        return n - 1
                
            