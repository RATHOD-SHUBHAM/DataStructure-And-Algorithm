# -------- -------- ----- Undirected Graph -------- -------- -----

# --------------------------- BFS --------------------------------------------
from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        #Code here

        visited = [False] * V

        parent = -1

        for i in range(V):
            if visited[i] == False:
                cyclePresent = self.checkForCycle(i, parent, visited, V, adj)
                
                if cyclePresent:
                    return 1

        return 0

    def checkForCycle(self, i, parent, visited, V, adj):

        queue = [[i, parent]]


        while queue:
            
            node, parent_node = queue.pop(0)
            
            visited[node] = True
            
            for child in adj[node]:
                if child == parent_node:
                    continue
                
                if visited[child] == True:
                    return True
                
                queue.append((child, node))
                        
        return False


# -------- -------- ----- DFS --------------------------------------------
from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		
		visited = [False] * V

		parent = -1

		for i in range(V):
			if visited[i] == False:
				isCyclePresent = self.dfs(i, parent, visited, V, adj)

				if isCyclePresent:
					return 1

		return 0
        
        
	def dfs(self, i, parent, visited, V, adj):

		visited[i] = True

		for child in adj[i]:
			if visited[child] == False:
				isCyclePresent = self.dfs(child, i, visited, V, adj)
				
				if isCyclePresent:
					return True
			else:
				if child != parent:
					return True
					
		return False



# -------- -------- ----- Directed Graph -------- -------- -----

#  ------ ------ Track Path algorithm ------ ------ ------ ------

# TC: O(V + E) | SC : O(V)
def cycleInGraph(edges):
    n = len(edges)

    visited = [False] * n
    # keep track of current nodes ancestor
    track_path = [False] * n

    for node in range(len(edges)):
        # check if the node has been explored before
        if visited[node]:
            continue

        cyclePresent = detectCycle(node, edges, visited,  track_path)

        if cyclePresent:
            return True

    return False
        

def detectCycle(node, edges, visited, track_path):
    # mark the node as visited
    visited[node] = True
    # Node is being explored in current path
    track_path[node] = True

    for child in edges[node]:
        # if child is not visited
        if not visited[child]:
            cyclePresent = detectCycle(child, edges, visited, track_path)

            if cyclePresent:
                return True
        # if child is visited - check if the child was vivisted in same path
        elif track_path[child]:
            return True

    # remove node from path
    track_path[node] = False
    return False


#  ------ ------ Kahns algorithm ------ ------ ------ ------
# Tc: O(v+e) | Sc: O(n)

def cycleInGraph(edges):
    n = len(edges)
    
    indegree = [0] * n

    # get the indegree of each edge
    for i in range(n):
        for nei in edges[i]:
            indegree[nei] += 1

    # get the node with indegree 0
    queue = []
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    # reduce the indegree
    count = 0
    topo_sort = []
    while queue:
        node = queue.pop(0)

        for nei in edges[node]:
            indegree[nei] -= 1

            if indegree[nei] == 0:
                queue.append(nei)

        count += 1
        topo_sort.append(node)

    if count != n:
        return True
    else:
        return False

