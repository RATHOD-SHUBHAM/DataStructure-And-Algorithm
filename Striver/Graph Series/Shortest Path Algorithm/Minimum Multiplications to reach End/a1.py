'''
    Catch is getting the number of nodes.
    If we observe we see after 10**5 we perform mod
    
    
    so any number less than 10^5 when we mod with 10^5. we will get the same number there will be no change
    
    so we can have max 9999 node.
    
    -- Next we need to find minimum steps - ie shortest path
    
    -- We can use queue(BFS), but since the number is huge there are chances that we can TLE
    
'''

# ------------------------------------------------------------------------------------------

# BFS _ Queue

from typing import List
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        mod = 100000
        
        queue = [(0,start)] # level , start
        
        # if a node is already added, then we dont need to readd it
        # previously we would have found the smallest distance - new dist maybe same or greater - so there is no point in adding
        visited = set()
        
        while queue:
            level , node = queue.pop(0)
            
            if node == end:
                return level
            
            visited.add(node)
            
            '''
                nei node is obtained by multiplying the node with number in the array and then mod operation with 100000
            '''
            for nei in arr:
                nei_node = (node * nei) % mod
                
                if nei_node in visited:
                    continue
                
                queue.append((level + 1, nei_node))
                
        return -1

# -----------------------------------------------------------------------------------------------

# Heapq - TLE

from typing import List
import heapq
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        mod = 100000
        
        minHeap = []
        heapq.heapify(minHeap)
        
        heapq.heappush(minHeap, (0,start))
        
        # if a node is already added, then we dont need to readd it
        # previously we would have found the smallest distance - new dist maybe same or greater - so there is no point in adding
        visited = set()
        
        while minHeap:
            level , node = heapq.heappop(minHeap)
            
            if node == end:
                return level
            
            visited.add(node)
            
            '''
                nei node is obtained by multiplying the node with number in the array and then mod operation with 100000
            '''
            for nei in arr:
                nei_node = (node * nei) % mod
                
                if nei_node in visited:
                    continue
                
                heapq.heappush(minHeap, (level + 1, nei_node))
                
        return -1

# -----------------------------------------------------------------------------------------------

# Dijkstras

from typing import List
import heapq, math
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        mod = 100000
        
        minHeap = []
        heapq.heapify(minHeap)
        
        heapq.heappush(minHeap, (0,start))
        
        minDist = [math.inf] * (10**5)
        minDist[start] = 0

        
        while minHeap:
            level , node = heapq.heappop(minHeap)
            
            if node == end:
                return level
            
            '''
                nei node is obtained by multiplying the node with number in the array and then mod operation with 100000
            '''
            for nei in arr:
                nei_node = (node * nei) % mod
                
                nei_dist = level + 1
                
                # if new smaller dist to reach the node is obtained
                if nei_dist < minDist[nei_node]:
                    minDist[nei_node] = nei_dist
                    heapq.heappush(minHeap, (nei_dist, nei_node))
                
        return -1