#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        #  code here
        n = len(arr)
        
        if n == 1:
            return 1
        
        # We sort arrivals and departures separately
        # This allows us to process the earliest arrival and earliest departure at each step
        arr.sort()
        dep.sort()
        
        pt1 = 0
        pt2 = 0
        
        platform_count = 0
        max_count = 0
        
        while pt1 < n and pt2 < n:
            # If a train is arriving before departure of train
            if arr[pt1] <= dep[pt2]:
                platform_count += 1
                pt1 += 1
            else:
                platform_count -= 1
                pt2 += 1
            
            max_count = max(max_count, platform_count)
        
        return max_count
