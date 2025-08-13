import collections 
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        
        n = len(adj)
        
        # BFS -> Queue
        op = []
        visited = set()
        
        queue = [0]
        visited.add(0)
        
        while queue:
            node = queue.pop(0)
            op.append(node)
            
            for child in adj[node]:
                if child not in visited:
                    visited.add(child)
                    queue.append(child)
            
        return op