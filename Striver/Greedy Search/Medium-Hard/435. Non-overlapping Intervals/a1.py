"""
The key insight is to use a greedy algorithm that keeps intervals with the earliest end times. Here's why this works:

    * Sort intervals by their end times
    * Always keep the interval that ends earliest among overlapping ones
    * This leaves maximum room for future non-overlapping intervals
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)

        # Sort by end time (key insight!)
        intervals.sort(key = lambda x : x[1])

        kept = 1
        prev_end_idx = intervals[0][1]

        for i in range(1, n):
            # If current interval doesn't overlap with the last kept interval
            if intervals[i][0] >= prev_end_idx:
                kept += 1
                prev_end_idx = intervals[i][1]
            # If it overlaps, we skip it (implicitly remove it)
        
        return kept

# ------------------------------ Remove -------------------------------
"""
The key insight is to use a greedy algorithm that keeps intervals with the earliest end times. Here's why this works:

    * Sort intervals by their end times
    * Always keep the interval that ends earliest among overlapping ones
    * This leaves maximum room for future non-overlapping intervals
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)

        # Sort by end time (key insight!)
        intervals.sort(key = lambda x : x[1])

        removed = 0
        prev_end_idx = intervals[0][1]

        for i in range(1, n):
            # If there's an overlap
            if intervals[i][0] < prev_end_idx:
                removed += 1 # Remove current interval
            else:
                prev_end_idx = intervals[i][1]
        
        return removed  