# Tc and Sc: O(V+E)

from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses

        # Step 1: Build graph
        graph = defaultdict(list)
        for edge in prerequisites:
            ai, bi = edge
            graph[bi].append(ai)
        
        # Step 2:  Get the indegree of nodes
        indegree = [0] * n
        for edge in prerequisites:
            ai, _ = edge
            indegree[ai] += 1
        
        # Step 3: Add the nodes with indegree = 0 to queue.
        queue = []
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        # Step 4: Topological sorting
        topo_sort = []
        count = 0

        while queue:
            node = queue.pop(0)

            # Grab neighbors and reduce their indegree.
            for nei in graph[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)

            topo_sort.append(node)
            count += 1
        
        if count != n:
            return []
        else:
            return topo_sort