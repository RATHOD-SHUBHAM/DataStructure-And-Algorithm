# https://leetcode.com/problems/course-schedule-ii/discuss/3541614/Kahn's-Algorithm-BFS-%2B-InDegree-*Python-Code*


# Tc | Sc : O(V+E)

from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = len(prerequisites)
        
        indegree = [0] * numCourses
        dic = defaultdict(list)
        
        for i in range(n):
            course, pre_req = prerequisites[i]
            
            indegree[course] += 1
            dic[pre_req].append(course)
            
        
        # print(indegree)
        
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                
        # print(queue)
        
        count = 0
        topo_sort = []
        
        while queue:
            node = queue.pop(0)
            
            for nei in dic[node]:
                indegree[nei] -= 1
                
                if indegree[nei] == 0:
                    queue.append(nei)
                    
            count += 1
            topo_sort.append(node)
            
        # print(count)
        # print(topo_sort)
        
        if count == numCourses:
            return True
        else:
            return False