# TLE

class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        mod = 100000
        
        queue = []
        queue.append((0,start))
        
        visited = set()
        
        while queue:
            level , node = queue.pop(0)
            
            if node == end:
                return level
                
            if node in visited:
                continue
            
            visited.add(node)
            
            for i in arr:
                cur_sum = (node * i) % mod
                queue.append((level + 1, cur_sum))
        
        # print(queue)
        return -1
