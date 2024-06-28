# --------------------------- Comapare all ---------------------------
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
    

# --------------------------- Move ON ---------------------------

# Tc: O(nlogn) + O(n) | Sc: O(n)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)

        intervals.sort(key = lambda x : x[0])

        merged_intervals = []

        for i in range(n):
            start , end = intervals[i]

            if len(merged_intervals) == 0 or merged_intervals[-1][1] < start:
                '''
                Non overlapping case:
                    1. When this is the first element
                    or
                    2. merged_intervals = [1,2], arr =[8,10]
                        2 < 8 -> so we check this and get to know
                '''
                merged_intervals.append([start, end])
            else:
                '''
                    Overlapping intervals
                        Check and Increase the size of window size if needed.
                '''
                merged_intervals[-1][1] = max(end, merged_intervals[-1][1])
        
        return merged_intervals