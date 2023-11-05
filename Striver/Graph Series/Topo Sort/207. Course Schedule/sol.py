# Kahn's Algorithm

'''
# https://leetcode.com/problems/course-schedule-ii/discuss/3541614/Kahn's-Algorithm-BFS-%2B-InDegree-*Python-Code*

# Node ordering
    bi needs to be completed before ai
    or
    bi needs to occur before ai

    so bi will point to ai
'''

# Tc | Sc : O(V+E)

from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
            return False
        else:
            return True