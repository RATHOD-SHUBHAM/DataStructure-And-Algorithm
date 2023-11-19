from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj_nei = defaultdict(list)
        
        # add all the neighbors to adjaccency list
        for parent , child in edges:
            adj_nei[parent].append(child)
            adj_nei[child].append(parent)
        
        # print(adj_nei)
        
        root = 0
        parentNode = -1
        
        return self.dfs(root , parentNode, adj_nei, hasApple)
        
    def dfs(self, node , parent, adj_nei, hasApple):
        minimum_time = 0

        # check all the neighbor
        for nei in adj_nei[node]:
            
            # if the neighbor is a parent then dont attend
            if nei == parent:
                continue

            child_minimum_time = self.dfs(nei , node, adj_nei, hasApple)

            # check the subtree and also check the the child nodes has apple
            if child_minimum_time or hasApple[nei]:
                minimum_time += 2 + child_minimum_time

        return minimum_time