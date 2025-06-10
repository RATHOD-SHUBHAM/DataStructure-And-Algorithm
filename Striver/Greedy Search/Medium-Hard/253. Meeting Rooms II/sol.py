# ============================= Greedy Wrong Answer =============================
"""
The issue with this approach is that I am only tracking one "previous" meeting, 
but I need to keep track of all active meeting rooms and their end times to properly assign meetings to available rooms.
"""

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)

        arr = sorted(intervals, key = lambda x : x[1])

        window = []

        prev_start_time = arr[0][0]
        prev_end_time = arr[0][1]

        for i in range(1, n):
            cur_start, cur_end = arr[i]

            # Can use the same meeting room
            if prev_end_time <= cur_start:
                prev_end_time = cur_end
            else:
                # Need a new meeting room
                window.append([prev_start_time, prev_end_time])
                prev_start_time = cur_start
                prev_end_time = cur_end
        
        window.append([prev_start_time, prev_end_time])

        print(window)

        return len(window)
    

# ============================= Heap Correct Answer =============================

# Tc: O(nlogn)
# Sc: O(n)

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)

        # Sort based on start time
        intervals.sort(key = lambda x : x[0]) # O(nlogn)

        min_heap = [] # keep track of meeting that will get over first

        for interval in intervals:
            start_time , end_time = interval

            if min_heap and min_heap[0] <= start_time:
                heapq.heappop(min_heap)
                
            heapq.heappush(min_heap, end_time)
        
        return len(min_heap)


