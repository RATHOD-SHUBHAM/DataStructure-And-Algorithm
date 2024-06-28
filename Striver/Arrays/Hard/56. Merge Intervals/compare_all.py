# Tc: O(nlogn) + O(2n) | Sc: O(n)

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)

        intervals.sort(key = lambda x : x[0])

        merged_intervals = []

        for i in range(n):
            start, end = intervals[i]

            # Check if the current interval is already a part of existing interval
            if merged_intervals and end <= merged_intervals[-1][1]:
                # We have sorted the array, so if the current end falls in between interval, it will be less than or equal to last element of interval
                continue

            # Check with remaining element.
            for j in range(i+1, n):
                nei_start, nei_end = intervals[j]

                if nei_start <= end:
                    end = max(nei_end , end)
            
            merged_intervals.append([start, end])
        

        return merged_intervals