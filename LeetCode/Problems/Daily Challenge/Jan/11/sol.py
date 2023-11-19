from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj_list = defaultdict(list)
        
        for parent, child in edges:
            adj_list[parent].append(child)
            adj_list[child].append(parent)
            
        root = 0
        parentNode = -1
        return self.dfs(root, parentNode, adj_list, hasApple)
    
    def dfs(self, node, parentNode, adj_list, hasApple):
        minimum_time = 0
        
        for nei in adj_list[node]:
            
            if nei == parentNode:
                continue
            
            child_minimum_time = self.dfs(nei, node, adj_list, hasApple)
            
            # check if subtree has min _time
            # check if children have apple
            if child_minimum_time > 0 or hasApple[nei]:
                minimum_time += 2 + child_minimum_time
                
        return minimum_time
        
        