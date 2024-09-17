# Tc|Sc: O(n)

class Solution:
    def timeTominutes(self, time:str)->int:
        hour, minute = map(int, time.split(':'))
        return hour * 60 + minute

    def findMinDifference(self, timePoints: List[str]) -> int:
        # Step1: Bucket Sort
        minutes = [False] * (24 * 60)

        for time in timePoints:
            minute = self.timeTominutes(time)

            # If same time exist twice - then min difference will be zero
            if minutes[minute] == True:
                return 0

            minutes[minute] = True
        # print(minutes)

        # Step2: Traversal
        min_diff = math.inf
        # Assign Pointers
        first_idx = last_idx = math.inf # Keep track of first and last time

        prev_idx = math.inf
        for cur_idx in range(len(minutes)):
            if minutes[cur_idx] == True:
                if prev_idx != math.inf:
                    diff = cur_idx - prev_idx
                    min_diff = min(min_diff, diff)
                    
                
                prev_idx = cur_idx
                
                # Check if this is the first timestamp
                if first_idx == math.inf:
                    first_idx = cur_idx
                
                # Keep track of last timestamp as well
                last_idx = cur_idx

        # Consider the [24hrs] + the first time captured and last[23:59]
        diff = ((24 * 60) + first_idx) - last_idx
        min_diff = min(min_diff, diff)
        
        # Convert minutes back to time
        return min_diff