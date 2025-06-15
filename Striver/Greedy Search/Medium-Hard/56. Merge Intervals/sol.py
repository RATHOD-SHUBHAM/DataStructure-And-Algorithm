# Tc: O(nlogn)
# Sc: O(n)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)

        intervals.sort(key = lambda x : (x[0], x[1]))

        output = []

        output.append(intervals[0])

        for i in range(1, n):
            cur_interval = intervals[i] # c,d
            prev_interval = output[-1] # a, b

            # check if there is a overlapping interval
            # if c <= b , there only there is a overlapping interval
            if cur_interval[0] <= prev_interval[1]:
                minRange = min(cur_interval[0], prev_interval[0])
                maxRange = max(cur_interval[1], prev_interval[1])

                output[-1] = [minRange, maxRange]
            else:
                output.append(cur_interval)
        
        return output