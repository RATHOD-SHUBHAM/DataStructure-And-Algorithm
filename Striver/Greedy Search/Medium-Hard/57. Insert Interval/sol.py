"""
Key Insights to Remember
1. Three distinct phases:
    * Before merge: Add intervals that end before newInterval starts
    * During merge: Merge all overlapping intervals
    * After merge: Add remaining intervals

2. Overlap condition:
    Two intervals [a,b] and [c,d] overlap if: a ≤ d and c ≤ b
        In our case: intervals[i][0] ≤ newInterval[1] (and we already know newInterval[0] ≤ intervals[i][1] from our loop condition)

3. The "expand and merge" technique:
    Instead of creating new intervals, we expand the newInterval to encompass all overlapping intervals, then add it once.
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)

        output = []

        minRange = newInterval[0]
        maxRange = newInterval[1]

        i = 0

        # Step 1: Add all intervals that end before newInterval starts
        while i < n and intervals[i][1] < minRange:
            output.append(intervals[i])
            i += 1
        
        # Step 2: Merge all overlapping intervals with newInterval
        while i < n and intervals[i][0] <= maxRange:
            # Expand newInterval to include the current interval
            minRange = min(intervals[i][0], minRange)
            maxRange = max(intervals[i][1], maxRange)
            i += 1
        
        # Add the merged interval
        output.append([minRange, maxRange])

        # Step 3: Add all remaining intervals
        while i < n:
            output.append(intervals[i])
            i += 1
        
        return output

        
