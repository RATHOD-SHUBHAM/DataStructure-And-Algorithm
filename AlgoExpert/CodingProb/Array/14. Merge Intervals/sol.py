# Tc: O(nlogn) | Sc: O(n)

def mergeOverlappingIntervals(intervals):
    # Write your code here.
    intervals.sort(key = lambda x:x[0])
    n = len(intervals)
    op = []

    # keep track of the previous interval
    prevInterval = intervals[0]

    for i in range(1, n):
        curInterval = intervals[i]

        # compare the current interval with previous interval
        if curInterval[0] <= prevInterval[1]:
            # merge the boundaries
            start = prevInterval[0]
            end = max(prevInterval[1] , curInterval[1])
            prevInterval = [start , end]
        # if non overlapping
        else:
            op.append(prevInterval)
            prevInterval = curInterval
            
    if prevInterval:
        op.append(prevInterval)
    
    return op
