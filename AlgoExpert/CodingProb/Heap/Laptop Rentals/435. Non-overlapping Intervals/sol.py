# Tc: O(nlogn)
# sc: O(1)

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        
        intervals.sort(key = lambda x : (x[0],x[1]))
        # print(intervals)
        
        # remove the largest interval to get the min number of intervals to be removed
        # hence keep track of the smallest intervals
        smallInterval = intervals[0]
        # print("firstInterval : ",firstInterval)
        
        removeIntervalCount = 0
        for idx in range(1 , len(intervals)):
            currentInterval = intervals[idx]
            
            # overlapping
            if currentInterval[0] < smallInterval[1]:
                removeIntervalCount += 1
                if currentInterval[1] < smallInterval[1]:
                    smallInterval = currentInterval
            # non overlapping    
            else:
                smallInterval = currentInterval # update the first interval to current Interval
                
        return removeIntervalCount