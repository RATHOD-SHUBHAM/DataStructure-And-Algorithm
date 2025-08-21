# Tc | Sc : O(V+E)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build graph
        graph = collections.defaultdict(list)

        for u, v in prerequisites:
            graph[v].append(u)

        
        # Step 1: Indegree of the node
        indegree = [0] * numCourses

        for u, v in prerequisites:
            indegree[u] += 1 
        
        # Step 2: Get the nodes with no pre req
        queue = collections.deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        # Step 3: Iterate and unlock the neighbors
        count = 0
        topo_sort = []

        while queue:
            node = queue.popleft()

            for nei in graph[node]:
                # Unlock the nei
                indegree[nei] -= 1

                # Check if there are no pre req left for the nei
                if indegree[nei] == 0:
                    queue.append(nei)
            
            count += 1
            topo_sort.append(node)
        

        if count == numCourses:
            return True
        else:
            return False