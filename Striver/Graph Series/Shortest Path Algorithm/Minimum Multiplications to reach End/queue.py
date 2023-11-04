# Queue - BFS
# TLE queue(BFS):  since the number is huge there are chances that we can TLE.


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
