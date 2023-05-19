# https://leetcode.com/problems/course-schedule-ii/discuss/3541614/Kahn's-Algorithm-BFS-%2B-InDegree-*Python-Code*

# topo sort = Kahns algo
# BFS + Indegree


# Tc and Sc: O(V+E)
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        no_of_course = numCourses - 1
        
        dic = defaultdict(list)
        for i in prerequisites:
            pre_req , course = i
            dic[pre_req].append(course)
        
        # print(dic)
        
        indegree = [0] * numCourses
        
        for i in prerequisites:
            pre_req , course = i
            indegree[course] += 1
            
        # print(indegree)
        
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                

        topo_sort = []
        count = 0
        
        while queue:
            node = queue.pop(0)
            
            # reduce the indegree of neighbors
            for nei in dic[node]:
                indegree[nei] -= 1
                
                if indegree[nei] == 0:
                    queue.append(nei)
                    
            count += 1
            topo_sort.append(node)
            
        # print(topo_sort)
        
        if count == numCourses:
            return topo_sort[::-1]
        else:
            return []