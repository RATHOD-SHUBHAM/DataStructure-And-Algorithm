import collections

class Solution:
	def isCycle(self, V, edges):
		graph = collections.defaultdict(list)
		
		for u, v in edges:
			graph[u].append(v)
			graph[v].append(u)
		
		visited = [False] * V
		
		for i in range(V):
			if visited[i] == True:
				continue
			
			parent = -1
			cyclePresent = self.dfs(i, parent, visited, graph)
			
			if cyclePresent == True:
				return True
		
		return False

	def dfs(self, node, parent, visited, graph):
		
		visited[node] = True
		
		for nei in graph[node]:
			if visited[nei] == True:
				if nei == parent:
					continue
				else:
					return True
			else:
				cyclePresent = self.dfs(nei, node, visited, graph)
			
				if cyclePresent == True:
					return True
		
		return False
				