# --------------- DFS --------------------------------------------------------
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
	
# --------------- BFS --------------------------------------------------------
	
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
                if visited[child] == False:
                    queue.append([child, node])
                else:
                    # a node can only be visited before if they have a common parent
                    if child != parent_node:
                        return True
                        
        return False