"""
Main Problems:
* Incorrect intersection tracking: You're only comparing the current train's arrival with the maximum departure time seen so far, but this doesn't properly track overlapping intervals.
* Wrong platform counting: You increment platform_count when trains overlap, but you never decrement it when trains depart. This means you're counting cumulative overlaps rather than simultaneous ones.
* Sorting limitation: You only sort by arrival time, but you need to process both arrivals and departures in chronological order to track the actual number of platforms in use at any moment.

Key Insights:
* Think of it as a timeline: At any point in time, count how many trains are simultaneously at the station.
* Process events chronologically: Sort arrivals and departures separately, then merge them in time order.
* Track current platforms: Increment when a train arrives, decrement when it departs.
* Handle edge case: When arrival and departure happen at the same time, the departure should be processed first (a train can depart and another can immediately use the same platform).
"""

#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        #  code here
        n = len(arr)
        
        if n == 1:
            return 1
        
        train_timing = []
        for i in range(n):
            train_timing.append([arr[i], dep[i]])
        
        train_timing.sort(key = lambda x : x[0])
        
        # Keep track of number of intersections
        platform_count = 0
        max_platform = 0
        
        # Keep track of time captured by train
        min_arr = train_timing[0][0]
        max_dep = train_timing[0][1]
        
        for i in range(1, n):
            cur_arr, cur_dep = train_timing[i]
            
            if cur_arr <= max_dep:
                platform_count += 1
                max_platform = max(max_platform, platform_count)
            
            min_arr = min(min_arr, cur_arr)
            max_dep = max(max_dep, cur_dep)
        
        return max_platform