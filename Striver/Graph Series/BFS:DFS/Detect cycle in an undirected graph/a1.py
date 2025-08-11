"""
Keep Track of parent Node because a edge from A -> B and B -> A is not a cycle.
This is also called a bidirectional edge.
"""

# --------------- DFS --------------------------------------------------------
import collections

class Solution:
    def isCycle(self, V, edges):
        #Code here
        visited = [False] * V

        # Create an Adjacency list
        adj_lst = collections.defaultdict(list)

        for u, v in edges:
            adj_lst[u].append(v)
            adj_lst[v].append(u)

        # Keep track of bidirectional edge
        # A - B and B - A is not an cycle
        parent = -1

        for i in range(V):
            if visited[i] == True:
                continue
            
            isConnected = self.dfs(i, parent, visited, adj_lst)
            
            # If cycle is detected
            if isConnected == True:
                return True
                
        return False

    def dfs(self, node, parent, visited, adj_lst):
        # Mark the node as visited
        visited[node] = True

        for nei in adj_lst[node]:
            # If neighbor is a parent, then this cant be a cycle, its a straight line
            if nei == parent:
                continue
            else:
                if visited[nei] == False:
                    isConnected = self.dfs(nei, node, visited, adj_lst)
                    
                    # If cycle is detected
                    if isConnected == True:
                        return True
                else:
                    # If the nei is already visited then there is a cycle
                    return True
                    
        return False
	
# --------------- BFS --------------------------------------------------------
	
import collections

class Solution:
    def isCycle(self, V, edges):
        #Code here
        visited = [False] * V
        
        # Create an Adjacency list
        adj_lst = collections.defaultdict(list)
        
        for u, v in edges:
            adj_lst[u].append(v)
            adj_lst[v].append(u)
        
        # Keep track of bidirectional edge
        # A - B and B - A is not an cycle
        parent = -1
        
        for i in range(V):
            if visited[i] == True:
                continue
            
            isConnected = self.bfs(i, parent, visited, adj_lst)
            
            # If cycle is detected
            if isConnected == True:
                return True
                
        return False
        
    def bfs(self, i, parent, visited, adj_lst):
        
        queue = collections.deque()
        queue.append((i, parent))
        
        visited[i] = True
        
        while queue:
            node, parent = queue.popleft()
            
            for nei in adj_lst[node]:
                # If neighbor is a parent, then this cant be a cycle, its a straight line
                if nei == parent:
                    continue
                else:
                    # In BFS cycle detection, it’s safest to mark visited when you enqueue a neighbor. That prevents the same node from being enqueued multiple times and causing false cycle signals.
                    if visited[nei] == False:
                        visited[nei] = True
                        queue.append((nei, node))
                    
                    else:
                        # If the nei is already visited then there is a cycle
                        return True
                    
        return False