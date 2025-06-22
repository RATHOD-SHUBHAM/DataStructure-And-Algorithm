#User function Template for python3

import heapq

# Heap logic
class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        n = len(arr)
        
        trains = []
        
        for i in range(n):
            trains.append([arr[i], dep[i]])
        
        trains.sort(key = lambda x : x[0])
        
        minHeap = []
        heapq.heapify(minHeap)
        
        heapq.heappush(minHeap, trains[0][1]) # Store only the departure time
        
        maxPlatforms = 1
        
        for i in range(1, n):
            st , et = trains[i]
            
            while minHeap and minHeap[0] < st:
                heapq.heappop(minHeap)
            
            heapq.heappush(minHeap, et)
            
            maxPlatforms = max(maxPlatforms , len(minHeap))
        
        return maxPlatforms
    