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