# Tc: O(nlogn)
# Sc: O(n)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)

        intervals.sort(key = lambda x : (x[0] , x[1]))

        op = []
        op.append(intervals[0])

        for i in range(1, n):
            minRange = op[-1][0]
            maxRange = op[-1][1]

            if intervals[i][0] <= maxRange:
                # minRange = min(minRange , intervals[i][0]) # since we have sorted, we can be sure, we will have minRange before
                maxRange = max(maxRange , intervals[i][1])
                op[-1] = [minRange, maxRange]
            else:
                op.append(intervals[i])
        
        return op
            
