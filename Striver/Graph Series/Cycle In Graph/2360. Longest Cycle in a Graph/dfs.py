class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)

        visited = [False] * n
        ancestor = [False] * n

        max_dist = -1

        for i in range(n):
            if visited[i] == True:
                continue
            
            dist = 0
            path_dist = {} # Keep track all nei distance from current node

            cycle = self.dfs(i, visited, ancestor, edges, path_dist, dist)

            if cycle > 0:
                max_dist = max(max_dist, cycle)
            
        return max_dist
    
    def dfs(self, node, visited, ancestor, edges, path_dist, dist):
        visited[node] = True
        ancestor[node] = True

        # add the node in the path
        path_dist[node] = dist

        # Explore neighbor
        nei = edges[node]

        # if there are no neighbor
        if nei == -1:
            ancestor[node] = False
            return 0
        

        # If the node is visited and is part of same cycle
        if visited[nei] == True and ancestor[nei] == True:
            ancestor[node] = False
            return (dist + 1) - path_dist[nei] # +1 because we need to take new dist of neighbor
        
        # Node is visited before but is not ancestor
        elif visited[nei] == True and ancestor[nei] == False:
            # Revisiting the same cycle again, wont make the cycle bigger
            ancestor[node] = False
            return 0

        else:
            new_dist = dist + 1
            cycle = self.dfs(nei, visited, ancestor, edges, path_dist, new_dist)
            ancestor[node] = False
            return cycle