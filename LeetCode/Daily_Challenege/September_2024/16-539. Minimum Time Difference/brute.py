# Tc: O(nlogn) | Sc: O(n)

import math
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # convert time to minute
        minutes = []

        for tme in timePoints:
            minute = (int(tme[ : 2]) * 60) + (int(tme[3: ]))
            minutes.append(minute)
        # print(minutes)

        minutes.sort()
        print(minutes)

        # Get Minimum difference
        min_diff = math.inf
        for i in range(1, len(minutes)):
            diff = minutes[i] - minutes[i - 1]
            min_diff = min(min_diff, diff)

        # Consider the [24hrs] + the first time captured and last[23:59]
        diff = ((24 * 60) + minutes[0]) - minutes[-1]
        min_diff = min(min_diff, diff)
        
        # Convert minutes back to time
        return min_diff



#  ------------------------ Same Solution ------------------------


class Solution:
    def timeTominutes(self, time:str)->int:
        hour, minute = map(int, time.split(':'))
        return hour * 60 + minute

    def findMinDifference(self, timePoints: List[str]) -> int:
        # convert time to minute
        minutes = [self.timeTominutes(time) for time in timePoints]
        # print(minutes)

        minutes.sort()
        print(minutes)

        # Get Minimum difference
        min_diff = math.inf
        for i in range(1, len(minutes)):
            diff = minutes[i] - minutes[i - 1]
            min_diff = min(min_diff, diff)

        # Consider the [24hrs] + the first time captured and last[23:59]
        diff = ((24 * 60) + minutes[0]) - minutes[-1]
        min_diff = min(min_diff, diff)
        
        # Convert minutes back to time
        return min_diff
