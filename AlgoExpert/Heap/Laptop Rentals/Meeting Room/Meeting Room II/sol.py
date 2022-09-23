# Tc: O(nlogn)
# Sc: O(n)

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return
        
        intervals.sort()
        
        minHeap = [intervals[0][1]]
        
        heapq.heapify(minHeap)
        print(minHeap)
        
        for i in range(1 , len(intervals)):
            st , et = intervals[i]
            
            if minHeap[0] <= st:
                heapq.heappop(minHeap)
                
            heapq.heappush(minHeap, et)
            
        return len(minHeap)
                
            