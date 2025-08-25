# --------------------- Kahns Algorithm ---------------------
# This will give TLE

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)

        indegree = [0] * n
        for i in range(n):
            x = edges[i]
            if x == -1:
                continue
            indegree[x] += 1
        

        queue = collections.deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        

        count = 0
        while queue:
            node = queue.popleft()

            nei = edges[node]

            if nei != -1:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)
            
            count +=1

        if count == n:
            # There is no cycle
            return -1
        else:
            max_len = -1
            for i in range(n):
                if indegree[i] == 0:
                    continue
                
                cur_len = self.detectCycle(i, edges)

                max_len = max(cur_len, max_len)
        
            return max_len
    
    def detectCycle(self, node, edges):
        visited = set()

        dist = 0

        while node not in visited:
            visited.add(node)
            dist += 1
            nei = edges[node]

            if nei != -1:
                node = nei
            else:
                break
        
        return dist
    
# --------------------- DFS + Ancestor Array ---------------------
    
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
            path_dist = {} # Keep track all path with nei distance from current node

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