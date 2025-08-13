import collections
class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        # code here
        n = len(adj)
        
        op = []
        visited = set()
        
        def helper(node):
            if node in visited:
                return
            
            op.append(node)
            visited.add(node)
            
            for child in adj[node]:
                helper(child)
        
        for i in range(n):
            if i not in visited:
                helper(i)
        
        return op
        